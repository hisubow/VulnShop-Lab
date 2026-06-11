import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_app(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    module.app.config.update(TESTING=True, SECRET_KEY="test")
    return module.app


def test_vulnerable_allows_normal_user_admin_access(monkeypatch, tmp_path):
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "vuln-admin.db"))
    app = load_app(ROOT / "vulnerable-app" / "app.py", "vuln_app_admin_test")
    client = app.test_client()
    client.post("/login", data={"username": "alice", "password": "alice123"})
    resp = client.get("/admin")
    assert resp.status_code == 200
    assert b"Admin Panel" in resp.data


def test_secure_blocks_normal_user_admin_access(monkeypatch, tmp_path):
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "secure-admin.db"))
    app = load_app(ROOT / "secure-app" / "app.py", "secure_app_admin_test")
    client = app.test_client()
    client.post("/login", data={"username": "alice", "password": "alice123"})
    resp = client.get("/admin")
    assert resp.status_code == 403


def test_secure_admin_does_not_render_password_hash(monkeypatch, tmp_path):
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "secure-admin-hash.db"))
    app = load_app(ROOT / "secure-app" / "app.py", "secure_app_no_hash_test")
    client = app.test_client()
    client.post("/login", data={"username": "admin", "password": "admin123"})
    resp = client.get("/admin")
    assert resp.status_code == 200
    assert b"password" not in resp.data.lower()
    assert b"scrypt" not in resp.data.lower()


def test_vulnerable_login_sqli_bypass_works_in_lab(monkeypatch, tmp_path):
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "vuln-sqli.db"))
    app = load_app(ROOT / "vulnerable-app" / "app.py", "vuln_app_sqli_test")
    client = app.test_client()
    payload = "' OR '1'='1' -- "
    resp = client.post("/login", data={"username": payload, "password": "anything"}, follow_redirects=False)
    assert resp.status_code == 302
    with client.session_transaction() as sess:
        assert sess.get("username") == "admin"


def test_secure_login_rejects_sqli_payload(monkeypatch, tmp_path):
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "secure-sqli.db"))
    app = load_app(ROOT / "secure-app" / "app.py", "secure_app_sqli_test")
    client = app.test_client()
    payload = "' OR '1'='1' -- "
    resp = client.post("/login", data={"username": payload, "password": "anything"}, follow_redirects=False)
    assert resp.status_code == 200
    with client.session_transaction() as sess:
        assert "username" not in sess


def test_vulnerable_search_reflects_raw_xss_payload(monkeypatch, tmp_path):
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "vuln-xss.db"))
    app = load_app(ROOT / "vulnerable-app" / "app.py", "vuln_app_xss_test")
    client = app.test_client()
    payload = '" onmouseover="alert(1)'
    resp = client.get("/search", query_string={"q": payload})
    assert resp.status_code == 200
    assert payload.encode() in resp.data


def test_secure_search_escapes_xss_payload(monkeypatch, tmp_path):
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "secure-xss.db"))
    app = load_app(ROOT / "secure-app" / "app.py", "secure_app_xss_test")
    client = app.test_client()
    payload = '" onmouseover="alert(1)'
    resp = client.get("/search", query_string={"q": payload})
    assert resp.status_code == 200
    assert payload.encode() not in resp.data
    assert b"&#34;" in resp.data or b"&quot;" in resp.data
