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

# ===========================
# Dashboard
# ===========================

PASSWORD = os.getenv("PASSWORD", "123456")

# ===========================
# Version
# ===========================

VERSION = "1.0.0"
