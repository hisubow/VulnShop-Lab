# Write-up: Missing Admin Authorization

## Summary

This write-up explains how a normal authenticated user can access the admin page in the vulnerable app and how the secure app prevents the same action.

## Affected area

- Vulnerable app: `http://localhost:5000/admin`
- Secure app: `http://localhost:5001/admin`
- User role used: `alice` / `user`

## Vulnerable behavior

In the vulnerable app, the `/admin` route only checks whether the user is logged in. It does not check whether the logged-in user has the `admin` role.

Expected secure behavior:

```text
A normal user should not be able to access admin-only functionality.
```

Observed vulnerable behavior:

```text
A normal user can open the admin page after login.
```

## Root cause

The vulnerable implementation performs authentication but not authorization. In other words, it asks:

```text
Is this user logged in?
```

but it does not ask:

```text
Is this user allowed to access admin functionality?
```

## Secure implementation

The secure app checks the role stored in the session before rendering the admin page. If the user is not an admin, the app returns `403 Forbidden`.

## Impact

If this bug existed in a real application, a normal user could view or modify administrative data. This is a Broken Access Control issue.

## Remediation

- Enforce server-side role checks for sensitive routes.
- Do not rely only on hiding buttons or links in the UI.
- Add tests that assert normal users receive `403 Forbidden` on admin endpoints.

## Retest result

- Vulnerable app: normal user can access `/admin`.
- Secure app: normal user receives `403 Forbidden`.
