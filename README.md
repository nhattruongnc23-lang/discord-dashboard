Discord Dashboard

Discord Dashboard là một dự án kết hợp giữa Discord Bot và Flask Web Dashboard, cho phép quản lý bot thông qua giao diện web.

Tính năng

- Hiển thị danh sách Server
- Hiển thị danh sách Channel
- Gửi tin nhắn từ Dashboard
- Hỗ trợ biến môi trường (.env)
- Sẵn sàng triển khai lên Render

Yêu cầu

- Python 3.14+
- Discord Bot Token

Cài đặt

pip install -r requirements.txt

Tạo file .env

TOKEN=YOUR_DISCORD_BOT_TOKEN
PASSWORD=123456

Chạy dự án

python app.py

Cấu trúc thư mục

discord-dashboard/
├── app.py
├── config.py
├── bot/
├── web/
├── static/
├── templates/
├── requirements.txt
└── README.md

Deploy

Nền tảng khuyến nghị: Render.

Tác giả

Nhat Truong
