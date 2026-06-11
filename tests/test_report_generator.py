import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_report_generator_outputs_markdown(tmp_path):
    spec = importlib.util.spec_from_file_location("report_generator", ROOT / "report-generator" / "generate_report.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["report_generator"] = module
    spec.loader.exec_module(module)
    data = module.load_evidence(ROOT / "examples" / "evidence-admin-auth.json")
    report = module.render_report(data)
    assert "Missing Admin Authorization" in report
    assert "VULN-07" in report
    assert "Remediation" in report
