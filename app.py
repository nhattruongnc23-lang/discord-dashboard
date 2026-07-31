from threading import Thread

from bot.client import start_bot
from web import create_app
from config import HOST, PORT

# Khởi động bot Discord
Thread(
    target=start_bot,
    daemon=True
).start()

# Khởi động Flask
app = create_app()

if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT
    )
