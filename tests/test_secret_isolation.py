"""WP1.2 — Secret / environment isolation for the Claude apply worker.

Static tests only. Does not invoke Claude Code, send email, submit applications,
or launch ApplyPilot Chrome.
"""

from __future__ import annotations

import json
import os
from unittest.mock import patch

import pytest

from applypilot.apply.secret_boundary import (
    SecretBoundaryError,
    build_apply_claude_env,
    build_gmail_mcp_env,
    build_playwright_mcp_env,
    cleanup_apply_runtime_files,
    redact_secrets_for_log,
    validate_apply_claude_env,
    validate_mcp_config_secret_boundary,
    validate_prompt_secret_boundary,
)


def test_claude_env_is_allowlist_not_full_parent(monkeypatch):
    """A/B/L: Claude env is allowlisted; unrelated parent secrets excluded."""
    monkeypatch.setenv("GEMINI_API_KEY", "fake-gemini-key-not-for-use")
    monkeypatch.setenv("OPENAI_API_KEY", "fake-openai-key-not-for-use")
    monkeypatch.setenv("CAPSOLVER_API_KEY", "fake-capsolver-key-not-for-use")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "fake-anthropic-key-not-for-use")
    monkeypatch.setenv("APPLYPILOT_UNRELATED_SECRET", "should-not-inherit")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///should-not-inherit")
    # Ensure PATH exists for process operation.
    if not os.environ.get("PATH") and not os.environ.get("Path"):
        monkeypatch.setenv("PATH", r"C:\Windows\System32")

    env = build_apply_claude_env()
    validate_apply_claude_env(env)

    assert env.get("APPLYPILOT_SECRET_BOUNDARY") == "1"
    assert "GEMINI_API_KEY" not in env
    assert "OPENAI_API_KEY" not in env
    assert "CAPSOLVER_API_KEY" not in env
    assert "ANTHROPIC_API_KEY" not in env
    assert "APPLYPILOT_UNRELATED_SECRET" not in env
    assert "DATABASE_URL" not in env
    assert env.get("PATH") or env.get("Path")


def test_required_runtime_vars_preserved(monkeypatch):
    """C: required non-secret runtime variables preserved when present."""
    monkeypatch.setenv("PATH", r"C:\Windows\System32;C:\Node")
    monkeypatch.setenv("USERPROFILE", r"C:\Users\TestUser")
    monkeypatch.setenv("APPDATA", r"C:\Users\TestUser\AppData\Roaming")
    monkeypatch.setenv("LOCALAPPDATA", r"C:\Users\TestUser\AppData\Local")
    monkeypatch.setenv("SystemRoot", r"C:\Windows")
    monkeypatch.setenv("TEMP", r"C:\Users\TestUser\AppData\Local\Temp")

    env = build_apply_claude_env()
    assert env["PATH"] == r"C:\Windows\System32;C:\Node"
    assert env["USERPROFILE"] == r"C:\Users\TestUser"
    assert env["APPDATA"].endswith("Roaming")
    assert env.get("SystemRoot") == r"C:\Windows"
    assert env.get("TEMP") == r"C:\Users\TestUser\AppData\Local\Temp"


def test_anthropic_api_key_stripped_for_max_plan(monkeypatch):
    """D: ANTHROPIC_API_KEY must not reach Claude (Max-plan auth path)."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-fake")
    monkeypatch.setenv("PATH", r"C:\Windows\System32")
    env = build_apply_claude_env()
    assert "ANTHROPIC_API_KEY" not in env
    # On-disk Claude login discovery needs a home profile path when available.
    # Whether Max auth succeeds is WP1.7 runtime validation.


def test_playwright_mcp_env_excludes_gmail_and_secrets(monkeypatch):
    """E: Playwright MCP env has no Gmail credential paths / CapSolver / LLM keys."""
    monkeypatch.setenv("PATH", r"C:\Windows\System32")
    monkeypatch.setenv("CAPSOLVER_API_KEY", "fake-capsolver")
    monkeypatch.setenv("GEMINI_API_KEY", "fake-gemini")
    base = build_apply_claude_env()
    pw = build_playwright_mcp_env(base)
    assert "GMAIL_CREDENTIALS_PATH" not in pw
    assert "GMAIL_OAUTH_PATH" not in pw
    assert "GMAIL_MCP_DIR" not in pw
    assert "CAPSOLVER_API_KEY" not in pw
    assert "GEMINI_API_KEY" not in pw
    assert "PLAYWRIGHT_MCP_ALLOW_UNRESTRICTED_FILE_ACCESS" not in pw


def test_gmail_mcp_env_excludes_provider_secrets(monkeypatch):
    """F: Gmail MCP env gets OAuth paths but not CapSolver/LLM/Anthropic API keys."""
    monkeypatch.setenv("PATH", r"C:\Windows\System32")
    monkeypatch.setenv("CAPSOLVER_API_KEY", "fake-capsolver")
    monkeypatch.setenv("OPENAI_API_KEY", "fake-openai")
    base = build_apply_claude_env()
    gm = build_gmail_mcp_env(base)
    assert "GMAIL_MCP_DIR" in gm
    assert "GMAIL_CREDENTIALS_PATH" in gm
    assert "GMAIL_OAUTH_PATH" in gm
    assert "CAPSOLVER_API_KEY" not in gm
    assert "OPENAI_API_KEY" not in gm
    assert "ANTHROPIC_API_KEY" not in gm
    assert "GEMINI_API_KEY" not in gm


def test_mcp_config_boundary_and_no_unrestricted_fs(monkeypatch):
    """E/F/I (config level): MCP config validates; Playwright not unrestricted."""
    monkeypatch.setenv("PATH", r"C:\Windows\System32")
    from applypilot.apply.launcher import _make_mcp_config

    with patch(
        "applypilot.apply.chrome.get_worker_viewport", return_value=(1280, 800)
    ), patch(
        "applypilot.apply.chrome._get_real_user_agent",
        return_value="Mozilla/5.0 TestAgent",
    ):
        cfg = _make_mcp_config(9222, worker_id=0)

    validate_mcp_config_secret_boundary(cfg)
    pw_args = cfg["mcpServers"]["playwright"]["args"]
    assert not any("allow-unrestricted-file-access" in a for a in pw_args)
    assert "GMAIL_CREDENTIALS_PATH" not in cfg["mcpServers"]["playwright"]["env"]
    assert "GMAIL_CREDENTIALS_PATH" in cfg["mcpServers"]["gmail"]["env"]
    assert "CAPSOLVER_API_KEY" not in json.dumps(cfg)


def test_prompt_excludes_password_and_capsolver(tmp_path, monkeypatch):
    """G/H: raw password + CapSolver capability absent from generated prompt."""
    from applypilot.apply import prompt as prompt_mod

    resume = tmp_path / "resume.pdf"
    resume.write_bytes(b"%PDF-1.4 fake")
    (tmp_path / "resume.txt").write_text("Experience building things", encoding="utf-8")

    profile = {
        "personal": {
            "full_name": "Test User",
            "email": "test.user@example.com",
            "phone": "555-0100",
            "password": "SuperSecretPassword!99",
            "city": "Austin",
            "province_state": "TX",
            "postal_code": "78701",
            "country": "USA",
            "address": "1 Main St",
        },
        "work_authorization": {
            "legally_authorized_to_work": "Yes",
            "require_sponsorship": "No",
        },
        "compensation": {
            "salary_expectation": "100000",
            "salary_range_max": "120000",
            "salary_currency": "USD",
        },
        "experience": {},
        "availability": {},
        "eeo_voluntary": {},
        "site_credentials": {
            "example.com": {
                "email": "test.user@example.com",
                "password": "SiteSecretPassword!88",
                "login_method": "email",
            }
        },
    }
    searches = {"location": {"primary": "Austin", "accept_patterns": ["Austin", "Remote"]}}

    monkeypatch.setenv("CAPSOLVER_API_KEY", "capsolver-should-not-appear")
    monkeypatch.setattr(prompt_mod.config, "load_profile", lambda: profile)
    monkeypatch.setattr(prompt_mod.config, "load_search_config", lambda: searches)
    monkeypatch.setattr(
        prompt_mod.config, "APPLY_WORKER_DIR", tmp_path / "workers"
    )
    monkeypatch.setattr(
        "applypilot.config.load_blocked_sso", lambda: ["accounts.google.com"]
    )
    monkeypatch.setattr(
        "applypilot.config.load_no_signup_domains", lambda: ["linkedin.com"]
    )
    monkeypatch.setattr(
        "applypilot.database.get_accounts_for_prompt", dict
    )
    monkeypatch.setattr(prompt_mod, "get_all_qa", lambda doc_format=None: [])
    monkeypatch.setattr(
        "applypilot.apply.chrome.detect_ats", lambda url: None
    )
    monkeypatch.setattr(
        "applypilot.apply.successful_paths.load_path", lambda slug: None
    )

    job = {
        "url": "https://example.com/jobs/1",
        "application_url": "https://example.com/jobs/1",
        "title": "Software Engineer",
        "site": "ExampleCo",
        "fit_score": 9,
        "tailored_resume_path": str(tmp_path / "resume"),
    }

    text = prompt_mod.build_prompt(
        job, tailored_resume="Experience building things", worker_id=0, dry_run=True
    )

    assert "SuperSecretPassword!99" not in text
    assert "SiteSecretPassword!88" not in text
    assert "capsolver-should-not-appear" not in text
    assert "https://api.capsolver.com/createTask" not in text
    assert "HCaptchaTaskProxyLess" not in text
    assert "You solve CAPTCHAs via the CapSolver" not in text
    assert "RESULT:NEEDS_HUMAN:captcha:" in text
    assert "passwords are NOT available" in text or "Passwords are NOT available" in text

    # Job-bound resume path under worker dir (I)
    worker_dir = tmp_path / "workers" / "worker-0"
    assert worker_dir.is_dir()
    assert any(p.name.endswith("_Resume.pdf") for p in worker_dir.iterdir())
    resume_line = next(ln for ln in text.splitlines() if "Resume PDF" in ln)
    assert "worker-0" in resume_line.replace("\\", "/")


def test_temp_runtime_files_cleaned(tmp_path):
    """J: temporary secret-bearing runtime files removed by cleanup helper."""
    mcp = tmp_path / "mcp-apply.json"
    settings = tmp_path / "claude-apply-settings.json"
    mcp.write_text('{"mcpServers":{}}', encoding="utf-8")
    settings.write_text('{"permissions":{}}', encoding="utf-8")
    cleanup_apply_runtime_files(mcp, settings)
    assert not mcp.exists()
    assert not settings.exists()


def test_redact_and_no_env_dump():
    """K: logging helper redacts credential-like strings / env dumps."""
    sample = "password=SuperSecret token=abc123"
    out = redact_secrets_for_log(sample)
    assert "SuperSecret" not in out
    assert "[REDACTED]" in out

    dump = "APPLYPILOT_SECRET_BOUNDARY=1 PATH=C:\\Windows GEMINI_API_KEY=x"
    assert redact_secrets_for_log(dump) == "[REDACTED: environment dump suppressed]"


def test_fail_closed_without_allowlist_marker():
    """L: broad inheritance without allowlist marker is rejected."""
    with pytest.raises(SecretBoundaryError, match="allowlist"):
        validate_apply_claude_env({"PATH": r"C:\\Windows", "GEMINI_API_KEY": "x"})


def test_fail_closed_missing_path():
    with pytest.raises(SecretBoundaryError, match="PATH"):
        build_apply_claude_env(parent_env={"USERPROFILE": r"C:\\Users\\x"})


def test_fail_closed_mcp_unrestricted_flag():
    with pytest.raises(SecretBoundaryError, match="unrestricted"):
        validate_mcp_config_secret_boundary({
            "mcpServers": {
                "playwright": {
                    "args": ["@playwright/mcp@0.0.75", "--allow-unrestricted-file-access"],
                    "env": {},
                },
                "gmail": {"args": [], "env": {}},
            }
        })


def test_fail_closed_prompt_capsolver_capability():
    with pytest.raises(SecretBoundaryError, match="CapSolver"):
        validate_prompt_secret_boundary(
            "You solve CAPTCHAs via the CapSolver REST API\nclientKey: abc"
        )


def test_fail_closed_prompt_password_line():
    with pytest.raises(SecretBoundaryError, match="password"):
        validate_prompt_secret_boundary("Password: hunter2\n")
