# ============================================================
#                  MEOW MEOW CONTROL PANEL
# ------------------------------------------------------------
# Chức năng:
# Quản lý đăng nhập và đăng xuất.
# ============================================================

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from modules.auth import login as login_user

# ==========================
# Blueprint
# ==========================

login = Blueprint("login", __name__)

# ==========================
# Trang đăng nhập
# ==========================

@login.route("/login")
def login_page():

    return render_template("login.html")

# ==========================
# Xử lý đăng nhập
# ==========================

@login.route("/login", methods=["POST"])
def login_post():

    username = request.form.get("username", "").strip()

    password = request.form.get("password", "")

    user = login_user(username, password)

    if user is None:

        flash("Tên đăng nhập hoặc mật khẩu không đúng.", "danger")

        return redirect(url_for("login.login_page"))

    session["user"] = user

    return redirect(url_for("dashboard.dashboard_home"))

# ==========================
# Đăng xuất
# ==========================

@login.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login.login_page"))
