# Code Comparison - English

This document helps learners understand the difference between vulnerable and secure code.

## Missing Admin Authorization

### Vulnerable idea

The app checks whether the user is logged in, but does not check the user's role.

```python
if "user_id" not in session:
    return redirect(url_for("login"))
return render_template("admin.html")
```

### Secure idea

The app verifies the `admin` role before allowing access.

```python
if "user_id" not in session:
    return redirect(url_for("login"))
if session.get("role") != "admin":
    abort(403)
```

## SQL Injection in Login

### Vulnerable idea

User input is concatenated directly into the SQL query.

```python
query = f"SELECT ... WHERE username = '{username}' AND password = '{password}'"
```

### Secure idea

Use a parameterized query.

```python
cur.execute("SELECT ... WHERE username = ?", (username,))
```

## Weak Password Storage

### Vulnerable idea

Passwords are stored in plaintext.

### Secure idea

Passwords are hashed and verified with `check_password_hash`.

---

## VULN-08 - CSRF Settings Update

### Vulnerable pattern

The vulnerable app accepts a state-changing `POST /settings` request without verifying a CSRF token.

```python
email = request.form.get("email", "")
conn.execute("UPDATE users SET email = ? WHERE id = ?", (email, session["user_id"]))
```

### Secure pattern

The secure app requires a token stored in the session and submitted with the form.

```python
token = request.form.get("csrf_token", "")
if not token or token != session.get("csrf_token"):
    abort(403)
```

### Lesson

State-changing actions should include server-side CSRF validation, even when the user is already authenticated.
