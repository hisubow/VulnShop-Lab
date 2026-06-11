from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_docker_compose_uses_separate_networks():
    compose_path = ROOT / "docker-compose.yml"
    assert compose_path.exists(), "docker-compose.yml should exist"

    content = compose_path.read_text(encoding="utf-8")

    assert "vulnshop_vulnerable_net" in content
    assert "vulnshop_secure_net" in content

    vulnerable_service_block = content.split("secure-app:")[0]
    secure_service_block = content.split("secure-app:")[1].split("volumes:")[0]

    assert "vulnshop_vulnerable_net" in vulnerable_service_block
    assert "vulnshop_secure_net" not in vulnerable_service_block

    assert "vulnshop_secure_net" in secure_service_block
    assert "vulnshop_vulnerable_net" not in secure_service_block


def test_docker_compose_exposes_localhost_ports():
    compose_path = ROOT / "docker-compose.yml"
    assert compose_path.exists(), "docker-compose.yml should exist"

    content = compose_path.read_text(encoding="utf-8")

    assert '"5000:5000"' in content or "'5000:5000'" in content
    assert '"5001:5000"' in content or "'5001:5000'" in content