import os
from dotenv import load_dotenv

load_dotenv()

LTA_API_KEY = os.getenv("LTA_API_KEY")

BASE_URL = "https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival"

HEADERS = {
    "AccountKey": LTA_API_KEY,
    "accept": "application/json"
}

RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"