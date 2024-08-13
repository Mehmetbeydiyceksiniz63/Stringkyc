from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22659994"))
API_HASH = getenv("API_HASH", "2c89964a0088a7a39ec819c60ae67de7")

BOT_TOKEN = getenv("BOT_TOKEN", "7439639831:AAGVCRa7TNt5Gh5vhw2FRNeFubTHeA-w6qI")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ihsantopic:ihsanbot@cluster0.jfejxle.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", "6604501109"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kumsalmuzikk")
