import importlib.util
import sys
import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_report_generator():
    spec = importlib.util.spec_from_file_location("report_generator", ROOT / "report-generator" / "generate_report.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["report_generator"] = module
    spec.loader.exec_module(module)
    return module


def test_report_generator_outputs_markdown():
    module = load_report_generator()
    data = module.load_evidence(ROOT / "examples" / "evidence-admin-auth.json")
    report = module.render_report(data)
    assert "Missing Admin Authorization" in report
    assert "VULN-07" in report
    assert "Remediation" in report


def test_report_generator_validates_required_fields():
    module = load_report_generator()
    incomplete = {"title": "Incomplete finding"}
    with pytest.raises(ValueError, match="missing required field"):
        module.render_report(incomplete)
