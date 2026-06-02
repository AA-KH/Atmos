from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
DEFAULT_COUNTRY = os.getenv("DEFAULT_COUNTRY")
DEFAULT_CITY = os.getenv("DEFAULT_CITY")
LOG_LEVEL = os.getenv("LOG_LEVEL")