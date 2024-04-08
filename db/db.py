from os import getenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


### MongoDB Stuff
db_user = getenv("DBUSER")
db_pass = getenv("DBPASS")  
uri = "mongodb+srv://"+str(db_user)+":"+str(db_pass)+"@cluster0.ebzle64.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["crossword-solver"]



# Collections 
user = db["users"]
puzzles = db["puzzles"]
uploaded_puzzles = db['user-uploaded-puzzles']
solved_puzzles = db['solved-puzzles']
