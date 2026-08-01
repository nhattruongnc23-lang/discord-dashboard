# ============================================================
#                  MEOW MEOW CONTROL PANEL
# ------------------------------------------------------------
# Chức năng:
# Hiển thị giao diện Dashboard.
# ============================================================

from flask import Blueprint, render_template

# ==========================
# Blueprint
# ==========================

dashboard = Blueprint("dashboard", __name__)

# ==========================
# Trang chủ Dashboard
# ==========================

@dashboard.route("/")
def dashboard_home():

    return render_template("dashboard.html")
