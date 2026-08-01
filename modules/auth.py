# ============================================================
#                  MEOW MEOW CONTROL PANEL
# ------------------------------------------------------------
# Chức năng:
# Xác thực tài khoản người dùng.
#
# Bao gồm:
# • Kiểm tra đăng nhập
# • Kiểm tra mật khẩu
# • Đăng xuất (sẽ thêm sau)
# ============================================================

# ==========================
# Thư viện
# ==========================

from werkzeug.security import check_password_hash

from database import connect


# ==========================
# Kiểm tra đăng nhập
# ==========================

def login(username, password):
    """
    Kiểm tra tên đăng nhập và mật khẩu.
    """

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username,
            password,
            role
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        return None

    if not check_password_hash(user[2], password):
        return None

    return {
        "id": user[0],
        "username": user[1],
        "role": user[3]
    }
