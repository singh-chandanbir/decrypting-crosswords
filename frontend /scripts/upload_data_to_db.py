from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

file = "../config.json"
configuration = open(file)
data = json.load(configuration)
db_user = data['db_username']
db_pass =data['db_pass']
configuration.close()


uri = "mongodb+srv://"+str(db_user)+":"+str(db_pass)+"@cluster0.ebzle64.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
mydb = client["crossword-solver"]
mycol = mydb["puzzles"]

# loop

# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)



for i in range (10746, 16746):

    existing_document = mycol.find_one({"number": i})
   

    if not existing_document:
        path = "../../data/puzzles/json/quick" + str(i)+ ".json"
        with open(path) as puzzles:
            puzzles_data = json.load(puzzles)
            result = mycol.insert_one(puzzles_data)
            print(f"Document inserted with ID: {result.inserted_id}")
        puzzles.close()
    else:
        print("\n")
        print(f"Document with number {i} already exists.")


