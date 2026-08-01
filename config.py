import os
from dotenv import load_dotenv

load_dotenv()

# ===========================
# Discord
# ===========================

TOKEN = os.getenv("TOKEN")

# ===========================
# Website
# ===========================

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 5000))
DEBUG = False

# ===========================
# Dashboard
# ===========================

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "123456")

# ===========================
# Application
# ===========================

APP_NAME = "Meow Meow Control Panel"
VERSION = "1.0.0"

# Flask Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
