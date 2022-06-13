from pymongo import MongoClient
import os
import bcrypt
from db import mongo_url

conn = MongoClient(mongo_url)

db= conn.get_database('sic')

user = db.user

password="123$123".encode('utf-8')

mySalt = bcrypt.gensalt()

user.insert_one({"username":"sanjay","password":bcrypt.hashpw(password, mySalt),"salt":mySalt})