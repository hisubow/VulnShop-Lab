import os
import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)
app.secret_key = os.getenv("VULNSHOP_SECRET_KEY", "dev-secret")
DB_PATH = os.getenv("VULNSHOP_DATABASE", "/app/instance/vulnshop.db")


def get_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, username TEXT, message TEXT)")
    cur.execute("DELETE FROM users")
    cur.execute("DELETE FROM products")
    cur.execute("DELETE FROM feedback")
    # INTENTIONAL VULNERABILITY: plaintext passwords for VULN-05.
    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", [
        (1, "admin", "admin123", "admin"),
        (2, "alice", "alice123", "user"),
        (3, "bob", "bob123", "user"),
    ])
    cur.executemany("INSERT INTO products VALUES (?, ?, ?)", [
        (1, "Mechanical Keyboard", 59.0),
        (2, "Wireless Mouse", 25.0),
        (3, "USB-C Hub", 35.0),
        (4, "Security Notebook", 9.0),
    ])
    cur.executemany("INSERT INTO feedback VALUES (?, ?, ?)", [(1, "admin", "Welcome to VulnShop-Lab!")])
    conn.commit()
    conn.close()


@app.before_request
def setup_once():
    if not getattr(app, "db_ready", False):
        init_db()
        app.db_ready = True


@app.route("/")
def home():
    return render_template("home.html", app_mode="Vulnerable App", badge_class="badge-danger", heading="VulnShop-Lab: Vulnerable App", description="This version intentionally contains insecure behavior for local learning.")


@app.route("/guide")
def guide():
    return render_template("guide.html", app_mode="Vulnerable App", badge_class="badge-danger", description="Use this app to observe vulnerable behavior, then compare it with the secure app.")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        conn = get_db()
        cur = conn.cursor()
        # INTENTIONAL VULNERABILITY: SQL Injection in Login for VULN-01.
        query = f"SELECT id, username, role FROM users WHERE username = '{username}' AND password = '{password}'"
        user = cur.execute(query).fetchone()
        conn.close()
        if user:
            session["user_id"] = user[0]
            session["username"] = user[1]
            session["role"] = user[2]
            return redirect(url_for("home"))
        flash("Invalid credentials")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route("/search")
def search():
    q = request.args.get("q", "")
    products = []
    if q:
        conn = get_db()
        cur = conn.cursor()
        # INTENTIONAL VULNERABILITY: SQL Injection in Search for VULN-02.
        query = f"SELECT id, name, price FROM products WHERE name LIKE '%{q}%'"
        try:
            products = cur.execute(query).fetchall()
        except sqlite3.Error:
            products = []
        conn.close()
    return render_template("search.html", q=q, products=products, unsafe_render=True)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        msg = request.form.get("message", "")
        username = session.get("username", "guest")
        conn = get_db()
        cur = conn.cursor()
        # INTENTIONAL VULNERABILITY: stored user content is rendered unsafely for VULN-04.
        cur.execute("INSERT INTO feedback(username, message) VALUES (?, ?)", (username, msg))
        conn.commit()
        conn.close()
        return redirect(url_for("feedback"))
    conn = get_db()
    items = conn.execute("SELECT id, username, message FROM feedback ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("feedback.html", feedback_items=items, unsafe_render=True)


@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))
    requested_id = request.args.get("id", session.get("user_id"))
    conn = get_db()
    # INTENTIONAL VULNERABILITY: IDOR for VULN-06, user-controlled ID is trusted.
    user = conn.execute(f"SELECT id, username, role FROM users WHERE id = {requested_id}").fetchone()
    conn.close()
    return render_template("profile.html", user=user)


@app.route("/admin")
def admin():
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_db()
    # INTENTIONAL VULNERABILITY: missing admin role check for VULN-07.
    # INTENTIONAL VULNERABILITY: exposes password storage style for VULN-05.
    users = conn.execute("SELECT id, username, role, password FROM users").fetchall()
    conn.close()
    return render_template("admin.html", users=users, show_passwords=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
