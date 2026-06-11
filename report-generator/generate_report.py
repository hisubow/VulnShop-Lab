import argparse
import json
from pathlib import Path
from datetime import datetime, timezone


def load_evidence(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def render_report(data: dict) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"""# Security Finding Report

Generated: {now}

## Summary

**Title:** {data.get('title', 'N/A')}  
**Vulnerability ID:** {data.get('vulnerability_id', 'N/A')}  
**Severity:** {data.get('severity', 'N/A')}  
**Affected Endpoint:** `{data.get('endpoint', 'N/A')}`  
**Test Account / Role:** {data.get('test_account', 'N/A')}

## Vulnerable Behavior

{data.get('vulnerable_behavior', 'N/A')}

## Secure Behavior / Retest Result

{data.get('secure_behavior', 'N/A')}

## Evidence

- Vulnerable App URL: `{data.get('vulnerable_url', 'N/A')}`
- Secure App URL: `{data.get('secure_url', 'N/A')}`
- Observed Status Code: `{data.get('status_code', 'N/A')}`
- Evidence Note: {data.get('evidence_note', 'N/A')}

## Root Cause

{data.get('root_cause', 'N/A')}

## Security Impact

{data.get('impact', 'N/A')}

## Remediation

{data.get('remediation', 'N/A')}

## Retest Notes

{data.get('retest_notes', 'N/A')}
"""


def main():
    parser = argparse.ArgumentParser(description="Generate a Markdown security finding report from evidence JSON.")
    parser.add_argument("evidence", help="Path to evidence JSON file")
    parser.add_argument("--output", default="reports/generated-report.md", help="Output Markdown path")
    args = parser.parse_args()

    evidence_path = Path(args.evidence)
    output_path = Path(args.output)
    data = load_evidence(evidence_path)
    report = render_report(data)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"[+] Report generated: {output_path}")


if __name__ == "__main__":
    main()
