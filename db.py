from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

mongo_url=os.environ.get("MONGO_URL")

conn = MongoClient(mongo_url)

db= conn.get_database('sic')

user = db.user