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
