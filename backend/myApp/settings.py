from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DBNAME = os.getenv("MONGO_DBNAME")
MONGO_URI = os.getenv("MONGO_URI")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")