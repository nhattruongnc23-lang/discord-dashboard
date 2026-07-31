from threading import Thread

from bot.client import start_bot
from web import create_app

# Khởi động bot Discord ở luồng riêng
Thread(
    target=start_bot,
    daemon=True
).start()

# Khởi động Flask
app = create_app()

if __name__ == "__main__":
    app.run()
