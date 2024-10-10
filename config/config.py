import os
from dotenv import load_dotenv

load_dotenv()

UID = os.getenv("UID")
SECRET = os.getenv("SECRET")
TOKEN_URL = os.getenv("TOKEN_URL")

BASE_URL = "https://api.intra.42.fr"
API_VERSION = "v2"