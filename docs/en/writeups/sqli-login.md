# Write-up: SQL Injection in Login

## Summary

This write-up explains why string-built SQL queries are unsafe and how parameterized queries prevent login bypass.

## Affected area

- Vulnerable app: `http://localhost:5000/login`
- Secure app: `http://localhost:5001/login`

## Vulnerable behavior

The vulnerable login route constructs a SQL query by inserting user-controlled input directly into the query string.

This means the database may interpret part of the input as SQL syntax instead of plain data.

## Root cause

The vulnerable pattern is:

```text
SQL query = fixed SQL text + raw user input
```

The safer pattern is:

```text
SQL query = parameterized SQL text + bound values
```

## Secure implementation

The secure app uses a parameterized query to look up the user and then verifies the password with a password-hashing helper.

## Impact

In a real application, SQL injection in login can lead to authentication bypass, account compromise, or data exposure depending on database privileges and query design.

## Remediation

- Use parameterized queries for all database access.
- Never concatenate raw user input into SQL.
- Store passwords with a strong password hashing mechanism.
- Add behavioral tests for known unsafe login patterns.

## Retest result

- Vulnerable app: unsafe login input can alter query behavior in the lab.
- Secure app: the same input is treated as data and rejected.
