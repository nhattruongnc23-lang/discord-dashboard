# ============================================================
#                  MEOW MEOW CONTROL PANEL
# ------------------------------------------------------------
# Chức năng:
# Khởi tạo Flask và đăng ký các Blueprint.
# ============================================================

from flask import Flask

from config import SECRET_KEY

# Blueprint
from web.routes.api import api
from web.routes.dashboard import dashboard
from web.routes.login import login
from web.routes.users import users
from web.routes.settings import settings


def create_app():

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    # ==========================
    # Khóa bảo mật Session
    # ==========================

    app.secret_key = SECRET_KEY

    # ==========================
    # Đăng ký Blueprint
    # ==========================

    app.register_blueprint(login)
    app.register_blueprint(dashboard)
    app.register_blueprint(api)
    app.register_blueprint(users)
    app.register_blueprint(settings)

    return app
