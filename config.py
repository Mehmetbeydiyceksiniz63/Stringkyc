from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 2930013))
API_HASH = getenv("API_HASH", "7cab92dcd979add511b79d693775e17d")

BOT_TOKEN = getenv("BOT_TOKEN", "6788830543:AAFtjCy0w9zjbi3CknH-zVBWik4mvwL9w4E")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://meyit31:Myt476331@cluster0.psvz6dk.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 1527476177))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/S1F1RB1RSOHBET")
