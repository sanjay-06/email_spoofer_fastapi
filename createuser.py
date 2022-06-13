from pymongo import MongoClient
import os
import bcrypt
from db import mongo_url
from dotenv import load_dotenv

load_dotenv()

conn = MongoClient(mongo_url)

db= conn.get_database('sic')

user = db.user

password=os.environ.get("YOUR_PASSWORD").encode('utf-8')

mySalt = bcrypt.gensalt()

user.insert_one({"username":os.environ.get("YOUR_USERNAME"),"password":bcrypt.hashpw(password, mySalt),"salt":mySalt})