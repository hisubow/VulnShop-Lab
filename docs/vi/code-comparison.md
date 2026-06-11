# Code Comparison - Tiếng Việt

Tài liệu này giúp người học hiểu sự khác nhau giữa code vulnerable và code secure.

## Missing Admin Authorization

### Vulnerable idea

App chỉ kiểm tra user đã đăng nhập hay chưa, nhưng không kiểm tra role.

```python
if "user_id" not in session:
    return redirect(url_for("login"))
return render_template("admin.html")
```

### Secure idea

App kiểm tra thêm role `admin` trước khi cho truy cập.

```python
if "user_id" not in session:
    return redirect(url_for("login"))
if session.get("role") != "admin":
    abort(403)
```

## SQL Injection in Login

### Vulnerable idea

Ghép trực tiếp input người dùng vào SQL query.

```python
query = f"SELECT ... WHERE username = '{username}' AND password = '{password}'"
```

### Secure idea

Dùng parameterized query.

```python
cur.execute("SELECT ... WHERE username = ?", (username,))
```

## Weak Password Storage

### Vulnerable idea

Lưu password dạng plaintext.

### Secure idea

Dùng password hash và kiểm tra bằng `check_password_hash`.
