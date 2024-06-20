from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 28920866))
API_HASH = getenv("API_HASH", "833ed2af149085968fff77d2fd843f51")

BOT_TOKEN = getenv("BOT_TOKEN", "7297331035:AAEyslXtWrvwEPdsWgGM382lUY8hZYszi-w")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ihsantopic:ihsanbot@cluster0.jfejxle.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 6563936773))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kiyicitayfaa")
