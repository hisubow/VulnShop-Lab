from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_docker_compose_uses_separate_internal_networks():
    content = (ROOT / "docker-compose.yml").read_text()
    assert "vulnshop_vulnerable_net" in content
    assert "vulnshop_secure_net" in content
    assert content.count("internal: true") >= 2
