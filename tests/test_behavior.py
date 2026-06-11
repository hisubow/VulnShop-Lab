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
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "vuln.db"))
    app = load_app(ROOT / "vulnerable-app" / "app.py", "vuln_app_test")
    client = app.test_client()
    client.post("/login", data={"username": "alice", "password": "alice123"})
    resp = client.get("/admin")
    assert resp.status_code == 200
    assert b"Admin Panel" in resp.data


def test_secure_blocks_normal_user_admin_access(monkeypatch, tmp_path):
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "secure.db"))
    app = load_app(ROOT / "secure-app" / "app.py", "secure_app_test")
    client = app.test_client()
    client.post("/login", data={"username": "alice", "password": "alice123"})
    resp = client.get("/admin")
    assert resp.status_code == 403


def test_secure_admin_does_not_render_password_hash(monkeypatch, tmp_path):
    monkeypatch.setenv("VULNSHOP_DATABASE", str(tmp_path / "secure_admin.db"))
    app = load_app(ROOT / "secure-app" / "app.py", "secure_app_admin_test")
    client = app.test_client()
    client.post("/login", data={"username": "admin", "password": "admin123"})
    resp = client.get("/admin")
    assert resp.status_code == 200
    assert b"password" not in resp.data.lower()
    assert b"scrypt" not in resp.data.lower()
