from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_compose():
    compose_path = ROOT / "docker-compose.yml"
    assert compose_path.exists(), "docker-compose.yml should exist"
    return yaml.safe_load(compose_path.read_text(encoding="utf-8"))


def test_docker_compose_uses_separate_networks():
    compose = load_compose()

    services = compose.get("services", {})
    networks = compose.get("networks", {})

    assert "vulnerable-app" in services
    assert "secure-app" in services

    assert "vulnshop_vulnerable_net" in networks
    assert "vulnshop_secure_net" in networks

    vulnerable_networks = services["vulnerable-app"].get("networks", [])
    secure_networks = services["secure-app"].get("networks", [])

    assert "vulnshop_vulnerable_net" in vulnerable_networks
    assert "vulnshop_secure_net" in secure_networks

    assert "vulnshop_secure_net" not in vulnerable_networks
    assert "vulnshop_vulnerable_net" not in secure_networks


def test_docker_compose_exposes_localhost_ports():
    compose = load_compose()
    services = compose.get("services", {})

    vulnerable_ports = services["vulnerable-app"].get("ports", [])
    secure_ports = services["secure-app"].get("ports", [])

    assert "5000:5000" in vulnerable_ports
    assert "5001:5000" in secure_ports