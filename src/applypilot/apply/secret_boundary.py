"""WP1.2 — least-privilege secret / environment boundary for apply workers.

Constructs explicit allowlisted environments for the Claude Code subprocess
and per-MCP child configuration. Fail closed: never silently fall back to
broad ``os.environ`` inheritance.
"""

from __future__ import annotations

import os
import re
from collections.abc import Mapping
from pathlib import Path


class SecretBoundaryError(RuntimeError):
    """Raised when the apply worker cannot establish a least-privilege secret boundary."""


# Marker proving the env was built by this module (not os.environ.copy()).
_BOUNDARY_MARKER = "APPLYPILOT_SECRET_BOUNDARY"
_BOUNDARY_MARKER_VALUE = "1"

# Non-secret runtime keys required for Windows process / Node / Claude Max auth
# material discovery under the user profile (credentials live on disk, not here).
_WINDOWS_RUNTIME_ALLOWLIST: frozenset[str] = frozenset({
    "ALLUSERSPROFILE",
    "APPDATA",
    "CommonProgramFiles",
    "CommonProgramFiles(x86)",
    "COMPUTERNAME",
    "ComSpec",
    "HOME",
    "HOMEDRIVE",
    "HOMEPATH",
    "LOCALAPPDATA",
    "NUMBER_OF_PROCESSORS",
    "OS",
    "Path",
    "PATH",
    "PATHEXT",
    "PROCESSOR_ARCHITECTURE",
    "PROCESSOR_IDENTIFIER",
    "PROCESSOR_LEVEL",
    "PROCESSOR_REVISION",
    "ProgramData",
    "ProgramFiles",
    "ProgramFiles(x86)",
    "PROMPT",
    "PUBLIC",
    "SESSIONNAME",
    "SystemDrive",
    "SystemRoot",
    "TEMP",
    "TMP",
    "USERDOMAIN",
    "USERDOMAIN_ROAMINGPROFILE",
    "USERNAME",
    "USERPROFILE",
    "windir",
    "WINDIR",
    # TLS / Node resolution (non-secret paths)
    "NODE_EXTRA_CA_CERTS",
    "SSL_CERT_FILE",
    "REQUESTS_CA_BUNDLE",
    "CURL_CA_BUNDLE",
    # Optional Claude config location override (path only)
    "CLAUDE_CONFIG_DIR",
    # Locale
    "LANG",
    "LANGUAGE",
    "LC_ALL",
    "LC_CTYPE",
})

# Exact prohibited keys that must never reach Claude / MCP apply children.
_PROHIBITED_ENV_EXACT: frozenset[str] = frozenset({
    "ANTHROPIC_API_KEY",
    "ANTHROPIC_AUTH_TOKEN",
    "ANTHROPIC_AWS_API_KEY",
    "ANTHROPIC_FOUNDRY_API_KEY",
    "ANTHROPIC_FOUNDRY_AUTH_TOKEN",
    "ANTHROPIC_CUSTOM_HEADERS",
    "GEMINI_API_KEY",
    "GOOGLE_API_KEY",
    "OPENAI_API_KEY",
    "DEEPSEEK_API_KEY",
    "LLM_API_KEY",
    "LLM_URL",
    "CAPSOLVER_API_KEY",
    "CAPSOLVER_API_BASE",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_ACCESS_KEY_ID",
    "AWS_SESSION_TOKEN",
    "GOOGLE_APPLICATION_CREDENTIALS",
    "DATABASE_URL",
    "CLAUDECODE",
    "CLAUDE_CODE_ENTRYPOINT",
})

# Name patterns for ambient secrets that must not be inherited.
_PROHIBITED_ENV_REGEX = re.compile(
    r"(?i)("
    r"API[_-]?KEY|SECRET|PASSWORD|PASSWD|TOKEN|PRIVATE[_-]?KEY|"
    r"CAPSOLVER|GEMINI|OPENAI|DEEPSEEK|"
    r"AWS_SECRET|AWS_ACCESS|"
    r"DATABASE_URL|CONNECTION_STRING"
    r")"
)

# Keys allowed on Gmail MCP only (paths to on-disk OAuth material).
_GMAIL_MCP_ENV_KEYS: frozenset[str] = frozenset({
    "GMAIL_MCP_DIR",
    "GMAIL_CREDENTIALS_PATH",
    "GMAIL_OAUTH_PATH",
})

# Keys that must never appear on Playwright MCP env blocks.
_PLAYWRIGHT_FORBIDDEN_ENV_KEYS: frozenset[str] = frozenset({
    *_GMAIL_MCP_ENV_KEYS,
    *_PROHIBITED_ENV_EXACT,
})

# Markers of active CapSolver *capability* (not mere prohibition text).
_CAPSOLVER_PROMPT_MARKERS = (
    "https://api.capsolver.com/createTask",
    "https://api.capsolver.com/getTaskResult",
    "clientKey:",
    "CapSolver REST API",
    "You solve CAPTCHAs via the CapSolver",
    "HCaptchaTaskProxyLess",
    "ReCaptchaV2TaskProxyLess",
)

_REDACT_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(?i)(api[_-]?key|password|secret|token|authorization)\s*[:=]\s*\S+"),
    re.compile(r"(?i)(bearer\s+)[A-Za-z0-9._\-]+"),
    re.compile(r"(?i)(sk-[A-Za-z0-9]{8,})"),
)


def _is_prohibited_env_name(name: str) -> bool:
    upper = name.upper()
    if upper in {k.upper() for k in _PROHIBITED_ENV_EXACT}:
        return True
    if name == _BOUNDARY_MARKER:
        return False
    if upper in {k.upper() for k in _WINDOWS_RUNTIME_ALLOWLIST}:
        return False
    if upper in {k.upper() for k in _GMAIL_MCP_ENV_KEYS}:
        # Gmail path keys belong only on the Gmail MCP env block, not Claude.
        return True
    if name.startswith("APPLYPILOT_"):
        # Product control flags may be allowlisted explicitly later; default deny.
        return name != _BOUNDARY_MARKER
    return bool(_PROHIBITED_ENV_REGEX.search(name))


def build_apply_claude_env(
    parent_env: Mapping[str, str] | None = None,
) -> dict[str, str]:
    """Build an explicit least-privilege environment for the Claude apply worker.

    Does **not** copy the full parent environment. Only allowlisted runtime keys
    are copied. CapSolver / LLM provider keys and other ambient secrets are
    excluded. ``ANTHROPIC_API_KEY`` is never passed (Max-plan auth uses on-disk
    Claude login under the user profile — REQUIRES CONTROLLED RUNTIME VALIDATION
    on hosts with Claude Code installed).
    """
    source = dict(parent_env) if parent_env is not None else dict(os.environ)
    # Windows env names are case-insensitive; normalize lookup.
    source_upper = {k.upper(): (k, v) for k, v in source.items()}
    env: dict[str, str] = {}

    for key in _WINDOWS_RUNTIME_ALLOWLIST:
        hit = source_upper.get(key.upper())
        if hit is None:
            continue
        _orig, val = hit
        if val is not None and val != "":
            # Preserve the canonical allowlist spelling for stability in tests.
            env[key] = val

    # PATH is mandatory for resolving ``claude`` / ``npx``.
    if not env.get("PATH") and not env.get("Path"):
        raise SecretBoundaryError(
            "Apply worker environment missing PATH; refusing to launch with "
            "incomplete process environment"
        )

    # Never allow these even if somehow listed above.
    for bad in _PROHIBITED_ENV_EXACT:
        env.pop(bad, None)

    env[_BOUNDARY_MARKER] = _BOUNDARY_MARKER_VALUE
    validate_apply_claude_env(env)
    return env


def validate_apply_claude_env(env: Mapping[str, str]) -> None:
    """Fail closed if the Claude env is broad or contains prohibited secrets."""
    if env.get(_BOUNDARY_MARKER) != _BOUNDARY_MARKER_VALUE:
        raise SecretBoundaryError(
            "Apply worker Claude environment must be built by "
            "build_apply_claude_env (allowlist); refusing broad inheritance"
        )

    if not env.get("PATH") and not env.get("Path"):
        raise SecretBoundaryError(
            "Apply worker Claude environment missing PATH"
        )

    for key in env:
        if key == _BOUNDARY_MARKER:
            continue
        if key in _GMAIL_MCP_ENV_KEYS:
            raise SecretBoundaryError(
                f"Refusing Gmail credential path env on Claude process: {key}"
            )
        # Allowlist keys are checked first inside _is_prohibited_env_name.
        if (
            key not in _WINDOWS_RUNTIME_ALLOWLIST
            and (key in _PROHIBITED_ENV_EXACT or _is_prohibited_env_name(key))
        ):
            raise SecretBoundaryError(
                f"Prohibited environment key present in Claude env: {key}"
            )

    # Size guard: a full user env is typically 50–200+ keys; allowlist is smaller.
    # Fail if someone stubs the marker onto a near-full copy.
    non_marker = [k for k in env if k != _BOUNDARY_MARKER]
    if len(non_marker) > len(_WINDOWS_RUNTIME_ALLOWLIST):
        raise SecretBoundaryError(
            "Claude environment exceeds allowlist size; refusing broad inheritance"
        )


def build_playwright_mcp_env(base_env: Mapping[str, str]) -> dict[str, str]:
    """Least-privilege env block for Playwright MCP (no Gmail / CapSolver / LLM keys)."""
    env = {
        k: v for k, v in base_env.items()
        if k != _BOUNDARY_MARKER and k not in _PLAYWRIGHT_FORBIDDEN_ENV_KEYS
    }
    # Explicitly keep unrestricted file access unset/false (default deny).
    env.pop("PLAYWRIGHT_MCP_ALLOW_UNRESTRICTED_FILE_ACCESS", None)
    for bad in _PLAYWRIGHT_FORBIDDEN_ENV_KEYS:
        if bad in env:
            raise SecretBoundaryError(
                f"Playwright MCP env must not include {bad}"
            )
    return env


def build_gmail_mcp_env(base_env: Mapping[str, str]) -> dict[str, str]:
    """Least-privilege env block for Gmail MCP (paths to OAuth files only extras)."""
    env = {
        k: v for k, v in base_env.items()
        if k != _BOUNDARY_MARKER and k not in _PROHIBITED_ENV_EXACT
    }
    for bad in _PROHIBITED_ENV_EXACT:
        env.pop(bad, None)

    gmail_dir = Path.home() / ".gmail-mcp"
    env["GMAIL_MCP_DIR"] = str(gmail_dir)
    env["GMAIL_CREDENTIALS_PATH"] = str(gmail_dir / "credentials.json")
    env["GMAIL_OAUTH_PATH"] = str(gmail_dir / "gcp-oauth.keys.json")

    for bad in ("CAPSOLVER_API_KEY", "GEMINI_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        if bad in env:
            raise SecretBoundaryError(f"Gmail MCP env must not include {bad}")
    return env


def validate_mcp_config_secret_boundary(mcp_config: Mapping) -> None:
    """Fail closed if MCP config widens secret access beyond the WP1.2 design."""
    servers = mcp_config.get("mcpServers") or {}
    if not isinstance(servers, dict):
        raise SecretBoundaryError("MCP config missing mcpServers")

    playwright = servers.get("playwright") or {}
    gmail = servers.get("gmail") or {}

    pw_args = [str(a) for a in (playwright.get("args") or [])]
    if any("allow-unrestricted-file-access" in a for a in pw_args):
        raise SecretBoundaryError(
            "Playwright MCP must not enable --allow-unrestricted-file-access"
        )

    pw_env = playwright.get("env") or {}
    gm_env = gmail.get("env") or {}
    if not isinstance(pw_env, dict) or not isinstance(gm_env, dict):
        raise SecretBoundaryError("MCP server env blocks must be objects")

    for key in _GMAIL_MCP_ENV_KEYS:
        if key in pw_env:
            raise SecretBoundaryError(
                f"Playwright MCP env must not include Gmail key {key}"
            )

    for key in _PROHIBITED_ENV_EXACT:
        if key in pw_env or key in gm_env:
            raise SecretBoundaryError(
                f"MCP env must not include prohibited key {key}"
            )
        # Also reject secret values embedded in args (defense in depth).
        joined = " ".join(pw_args + [str(a) for a in (gmail.get("args") or [])])
        if key in joined:
            raise SecretBoundaryError(
                f"MCP args must not embed prohibited key name {key}"
            )

    if "CAPSOLVER_API_KEY" in pw_env or "CAPSOLVER_API_KEY" in gm_env:
        raise SecretBoundaryError("CapSolver credentials must not appear in MCP env")


def validate_prompt_secret_boundary(
    prompt: str,
    *,
    forbidden_substrings: list[str] | None = None,
) -> None:
    """Fail closed if the apply prompt contains prohibited raw secrets."""
    for marker in _CAPSOLVER_PROMPT_MARKERS:
        if marker in prompt:
            raise SecretBoundaryError(
                f"Apply prompt contains prohibited CapSolver material ({marker})"
            )

    for item in forbidden_substrings or []:
        if item and item in prompt:
            raise SecretBoundaryError(
                "Apply prompt contains a prohibited secret substring"
            )

    # Raw password lines from the inherited credential dump pattern.
    if re.search(r"(?im)^\s*Password:\s*\S+", prompt):
        raise SecretBoundaryError(
            "Apply prompt must not embed raw password values"
        )
    if re.search(r"(?i)/\s*password=[^\s]+", prompt):
        raise SecretBoundaryError(
            "Apply prompt must not embed password= credential pairs"
        )


def redact_secrets_for_log(text: str) -> str:
    """Best-effort redaction for logs/errors (not a general logging framework)."""
    if not text:
        return text
    redacted = text
    for pat in _REDACT_PATTERNS:
        redacted = pat.sub(lambda m: (m.group(1) if m.lastindex else "") + "[REDACTED]", redacted)
    # Never dump full env dict reprs.
    if "APPLYPILOT_SECRET_BOUNDARY" in redacted and "PATH=" in redacted:
        redacted = "[REDACTED: environment dump suppressed]"
    return redacted


def cleanup_apply_runtime_files(*paths: Path | str | None) -> None:
    """Remove temporary runtime config files that may describe MCP/settings."""
    for raw in paths:
        if not raw:
            continue
        path = Path(raw)
        try:
            if path.is_file():
                path.unlink()
        except OSError:
            pass
