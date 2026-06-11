import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

REQUIRED_FIELDS = [
    "title",
    "vulnerability_id",
    "severity",
    "endpoint",
    "test_account",
    "vulnerable_url",
    "secure_url",
    "status_code",
    "vulnerable_behavior",
    "secure_behavior",
    "evidence_note",
    "root_cause",
    "impact",
    "remediation",
    "retest_notes",
]


def load_evidence(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Evidence file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_evidence(data: dict) -> None:
    missing = [field for field in REQUIRED_FIELDS if not str(data.get(field, "")).strip()]
    if missing:
        fields = ", ".join(missing)
        raise ValueError(f"Evidence JSON is missing required field(s): {fields}")


def render_report(data: dict) -> str:
    validate_evidence(data)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"""# Security Finding Report

Generated: {now}

## Summary

**Title:** {data['title']}  
**Vulnerability ID:** {data['vulnerability_id']}  
**Severity:** {data['severity']}  
**Affected Endpoint:** `{data['endpoint']}`  
**Test Account / Role:** {data['test_account']}

## Vulnerable Behavior

{data['vulnerable_behavior']}

## Secure Behavior / Retest Result

{data['secure_behavior']}

## Evidence

- Vulnerable App URL: `{data['vulnerable_url']}`
- Secure App URL: `{data['secure_url']}`
- Observed Status Code: `{data['status_code']}`
- Evidence Note: {data['evidence_note']}

## Root Cause

{data['root_cause']}

## Security Impact

{data['impact']}

## Remediation

{data['remediation']}

## Retest Notes

{data['retest_notes']}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown security finding report from evidence JSON.")
    parser.add_argument("evidence", help="Path to evidence JSON file")
    parser.add_argument("--output", default="reports/generated-report.md", help="Output Markdown path")
    args = parser.parse_args()

    try:
        evidence_path = Path(args.evidence)
        output_path = Path(args.output)
        data = load_evidence(evidence_path)
        report = render_report(data)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report, encoding="utf-8")
        print(f"[+] Report generated: {output_path}")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"[-] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
