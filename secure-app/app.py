import os
import sqlite3
from pathlib import Path
from flask import Flask, render_template, request, redirect, session, url_for, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = Path(__file__).resolve().parent
COMMON_DIR = Path(os.getenv("VULNSHOP_COMMON_DIR", str(BASE_DIR.parent / "common")))

app = Flask(__name__, template_folder=str(COMMON_DIR / "templates"), static_folder=str(COMMON_DIR / "static"))
app.secret_key = os.getenv("VULNSHOP_SECRET_KEY", "dev-secret")
DB_PATH = os.getenv("VULNSHOP_DATABASE", "/app/instance/vulnshop.db")


def get_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT, role TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, username TEXT, message TEXT)")
    cur.execute("DELETE FROM users")
    cur.execute("DELETE FROM products")
    cur.execute("DELETE FROM feedback")
    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", [
        (1, "admin", generate_password_hash("admin123"), "admin"),
        (2, "alice", generate_password_hash("alice123"), "user"),
        (3, "bob", generate_password_hash("bob123"), "user"),
    ])
    cur.executemany("INSERT INTO products VALUES (?, ?, ?)", [
        (1, "Mechanical Keyboard", 59.0),
        (2, "Wireless Mouse", 25.0),
        (3, "USB-C Hub", 35.0),
        (4, "Security Notebook", 9.0),
    ])
    cur.executemany("INSERT INTO feedback VALUES (?, ?, ?)", [(1, "admin", "Welcome to the secure version of VulnShop-Lab!")])
    conn.commit()
    conn.close()



@app.route("/")
def home():
    return render_template("home.html", app_mode="Secure App", badge_class="badge-secure", heading="VulnShop-Lab: Secure App", description="This version demonstrates safer implementation patterns for comparison.")


@app.route("/guide")
def guide():
    return render_template("guide.html", app_mode="Secure App", badge_class="badge-secure", description="Use this app to compare fixed behavior with the vulnerable app.")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        conn = get_db()
        cur = conn.cursor()
        user = cur.execute("SELECT id, username, password_hash, role FROM users WHERE username = ?", (username,)).fetchone()
        conn.close()
        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]
            session["role"] = user[3]
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
        products = conn.execute("SELECT id, name, price FROM products WHERE name LIKE ?", (f"%{q}%",)).fetchall()
        conn.close()
    return render_template("search.html", q=q, products=products, unsafe_render=False)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        msg = request.form.get("message", "")
        username = session.get("username", "guest")
        conn = get_db()
        conn.execute("INSERT INTO feedback(username, message) VALUES (?, ?)", (username, msg))
        conn.commit()
        conn.close()
        return redirect(url_for("feedback"))
    conn = get_db()
    items = conn.execute("SELECT id, username, message FROM feedback ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("feedback.html", feedback_items=items, unsafe_render=False)


@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))
    requested_id = request.args.get("id", str(session.get("user_id")))
    if session.get("role") != "admin" and str(requested_id) != str(session.get("user_id")):
        abort(403)
    conn = get_db()
    user = conn.execute("SELECT id, username, role FROM users WHERE id = ?", (requested_id,)).fetchone()
    conn.close()
    return render_template("profile.html", user=user)


@app.route("/admin")
def admin():
    if "user_id" not in session:
        return redirect(url_for("login"))
    if session.get("role") != "admin":
        abort(403)
    conn = get_db()
    users = conn.execute("SELECT id, username, role FROM users").fetchall()
    conn.close()
    return render_template("admin.html", users=users, show_passwords=False)


# Initialize database once when the application process starts.
# This avoids per-request initialization and keeps the lab deterministic.
init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
