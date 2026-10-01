# 🗿  Visit & Support us - @UHD_NETWORK
# ⚡️ Do Not Remove Credit - Made by @UHDBots
# 💬 For Any Help Join Support Group: @UHDBots_Support
# 🚫 Removing or Modifying these Lines will Cause the bot to Stop Working.


import re
from os import environ


id_pattern = re.compile(r'^-?\d+$')


SESSION = environ.get("SESSION", "UHDFiletoLinksBot")
API_ID = int(environ.get("API_ID", "12850056"))
API_HASH = environ.get("API_HASH", "15564ec4a1a2cbef87c99a9aa9e40b34")
BOT_TOKEN = environ.get("BOT_TOKEN", "8840797536:AAEQvXXXXYq6GEj5SKgwc3wQpQILEeHDWv8")


PORT = int(environ.get("PORT", "8080"))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
ON_HEROKU = "DYNO" in environ
URL = environ.get("URL", "")


LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "0"))
ADMINS = [
    int(admin) if id_pattern.match(admin) else admin
    for admin in environ.get("ADMINS", "770434685").split()
]


DATABASE_URI = environ.get("DATABASE_URI", "")
DATABASE_NAME = environ.get("DATABASE_NAME", "")
