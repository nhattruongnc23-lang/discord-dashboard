# ============================================================
#                  MEOW MEOW CONTROL PANEL
# ------------------------------------------------------------
# Chức năng:
# Quản lý cơ sở dữ liệu của hệ thống.
#
# File này chịu trách nhiệm:
# • Kết nối SQLite
# • Khởi tạo cơ sở dữ liệu
# • Tạo bảng tài khoản
#
# Tác giả : Trường Nhật
# Phiên bản : 1.0.0
# ============================================================

# ==========================
# Thư viện
# ==========================

import sqlite3

# ==========================
# Đường dẫn cơ sở dữ liệu
# ==========================

DATABASE = "data/users.db"

# ==========================
# Kết nối cơ sở dữ liệu
# ==========================

def connect():
    """
    Trả về kết nối tới SQLite.
    """

    return sqlite3.connect(DATABASE)

# ==========================
# Khởi tạo cơ sở dữ liệu
# ==========================

def create_database():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            role TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()

    conn.close()

# ==========================
# Chạy trực tiếp
# ==========================

if __name__ == "__main__":

    print("=" * 50)
    print(" MEOW MEOW CONTROL PANEL")
    print("=" * 50)

    print("Đang tạo cơ sở dữ liệu...")

    create_database()

    print("✔ Hoàn tất!")
    print("Cơ sở dữ liệu đã sẵn sàng.")
