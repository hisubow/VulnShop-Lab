from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_compose() -> str:
    compose_path = ROOT / "docker-compose.yml"
    assert compose_path.exists(), "docker-compose.yml should exist"
    return compose_path.read_text(encoding="utf-8")


def test_docker_compose_defines_separate_networks():
    content = read_compose()

    assert "vulnshop_vulnerable_net:" in content
    assert "vulnshop_secure_net:" in content

    assert "vulnerable-app:" in content
    assert "secure-app:" in content


def test_vulnerable_app_uses_vulnerable_network():
    content = read_compose()

    assert "vulnerable-app:" in content
    assert "- vulnshop_vulnerable_net" in content


def test_secure_app_uses_secure_network():
    content = read_compose()

    assert "secure-app:" in content
    assert "- vulnshop_secure_net" in content


def test_docker_compose_exposes_localhost_ports():
    content = read_compose()

    assert '"5000:5000"' in content or "'5000:5000'" in content
    assert '"5001:5000"' in content or "'5001:5000'" in content