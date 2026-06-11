# Release Notes

## v1.1.0 - Portfolio Polish

### Added

- Docker Compose network isolation with separate internal networks for vulnerable and secure services.
- VULN-08: Missing CSRF Protection on the account settings workflow.
- Session-based Guided Challenge Scoreboard at `/scoreboard`.
- Account Settings page at `/settings` for the CSRF learning module.
- Complete write-ups for:
  - Missing Admin Authorization
  - SQL Injection in Login
- Additional evidence example:
  - `examples/evidence-csrf-settings.json`
- Behavioral tests for:
  - CSRF behavior
  - Scoreboard progress tracking
  - Docker Compose network isolation

### Improved

- README now highlights network isolation, scoreboard, write-ups, and expanded tests.
- Challenge documentation now includes CSRF and report-generation tasks.
- Vulnerability list now includes VULN-08.
- Remediation guide includes CSRF protection guidance.

## v1.0.1 - Repository Polish

### Added

- Shared `common/` templates and static assets.
- Additional evidence JSON examples.
- JSON validation in the report generator.
- Expanded behavioral tests.
- Release notes documentation.

### Changed

- Removed tracked generated Python cache files from the project package.
- Removed GitHub upload guide from the public documentation.
- Replaced duplicated templates/static assets with shared common assets.

## v1.0.0 - Initial Stable Release

Initial stable release of VulnShop-Lab as a Dockerized web security learning platform.
