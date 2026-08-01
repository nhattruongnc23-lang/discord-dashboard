# ============================================================
#                  MEOW MEOW CONTROL PANEL
# ------------------------------------------------------------
# Chức năng:
# Tạo tài khoản Chủ sở hữu đầu tiên.
#
# Tài khoản sẽ được lưu vào cơ sở dữ liệu SQLite.
# Mật khẩu được mã hóa để đảm bảo an toàn.
# ============================================================

from getpass import getpass

from werkzeug.security import generate_password_hash

from database import connect


def create_owner():

    print("=" * 50)
    print(" TẠO TÀI KHOẢN CHỦ SỞ HỮU")
    print("=" * 50)

    username = input("Tên đăng nhập: ").strip()

    password = getpass("Mật khẩu: ")

    conn = connect()

    cursor = conn.cursor()

    # Kiểm tra tài khoản đã tồn tại chưa
    cursor.execute(
        "SELECT id FROM users WHERE username = ?",
        (username,)
    )

    if cursor.fetchone():

        print("\n❌ Tên đăng nhập đã tồn tại!")

        conn.close()

        return

    # Mã hóa mật khẩu
    password_hash = generate_password_hash(password)

    # Thêm tài khoản
    cursor.execute(
        """
        INSERT INTO users
        (
            username,
            password,
            role
        )
        VALUES
        (
            ?, ?, ?
        )
        """,
        (
            username,
            password_hash,
            "owner"
        )
    )

    conn.commit()

    conn.close()

    print("\n✅ Đã tạo tài khoản Chủ sở hữu thành công!")


if __name__ == "__main__":

    create_owner()
