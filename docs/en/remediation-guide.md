# Remediation Guide - English

## General Principles

- Do not concatenate user input into SQL queries.
- Do not render user-controlled data with `safe` unless there is a clear reason.
- Always enforce authorization on the backend.
- Do not store plaintext passwords.
- Do not trust object IDs from URLs without checking the current user.

## Vulnerability-to-Fix Mapping

| ID | Remediation |
|---|---|
| VULN-01 | Use parameterized queries and password hashing |
| VULN-02 | Use parameterized queries for search |
| VULN-03 | Escape output when rendering |
| VULN-04 | Escape stored user content |
| VULN-05 | Use password hashing such as Werkzeug password hashing |
| VULN-06 | Check object ownership or role |
| VULN-07 | Enforce role-based authorization |

## CSRF Protection

For state-changing requests such as profile updates, password changes, or account settings:

- Require a CSRF token for form submissions.
- Store the token server-side or bind it to the user session.
- Reject missing or invalid tokens with a clear authorization failure.
- Prefer framework-supported CSRF protection for real applications.
