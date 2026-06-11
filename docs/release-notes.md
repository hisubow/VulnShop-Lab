# Release Notes

## v1.0.1 - Repository Polish

This release focuses on repository quality and maintainability.

### Changed

- Removed generated Python cache files from the repository.
- Moved duplicated templates and static assets into a shared `common/` directory.
- Added more evidence JSON examples for common vulnerability classes.
- Added stronger behavioral tests for SQL Injection and XSS learning cases.
- Added validation to the Markdown report generator.
- Clarified the Reflected XSS / attribute injection edge case in the challenge documentation.

### Notes

The vulnerable application remains intentionally insecure and must only be used in local, authorized learning environments.
