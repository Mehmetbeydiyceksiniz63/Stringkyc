from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22659994"))
API_HASH = getenv("API_HASH", "2c89964a0088a7a39ec819c60ae67de7")

BOT_TOKEN = getenv("BOT_TOKEN", "7381395088:AAGCrCkgrNfP0AgIG4b5bz6HH6rj694utRY")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kurt67143:nays@cluster0.vjg7bma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", "7268753735"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kumsalmuzikk")
