from os import getenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


### MongoDB Stuff
uri = getenv("MONGO_URL")
client = MongoClient(uri, server_api=ServerApi("1"))
db = client["crossword-solver"]


# Collections
user = db["users"]
puzzles = db["puzzles"]
uploaded_puzzles = db["user-uploaded-puzzles"]
solved_puzzles = db["solved-puzzles"]
