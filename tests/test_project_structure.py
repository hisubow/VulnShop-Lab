from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_key_files_exist():
    required = [
        "README.md",
        "docker-compose.yml",
        ".env.example",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "LICENSE",
        "vulnerable-app/app.py",
        "secure-app/app.py",
        "common/templates/base.html",
        "common/static/style.css",
        "report-generator/generate_report.py",
        "docs/vi/challenges.md",
        "docs/en/challenges.md",
        "docs/release-notes.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

