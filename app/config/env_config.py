import os

TZ = os.getenv("TZ", "UTC")

MARKET_SYMBOLS = os.getenv("MARKET_SYMBOLS", "usdt").split(",")
QUOTE_CURRENCY = os.getenv("QUOTE_CURRENCY", "rls")

UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", "300"))

APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "5000"))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
