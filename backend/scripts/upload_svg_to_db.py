# from bson.binary import Binary
# import os
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# from dotenv import load_dotenv

# load_dotenv()
# db_user = os.getenv("DBUSER")
# db_pass = os.getenv("DBPASS")  


# uri = "mongodb+srv://"+str(db_user)+":"+str(db_pass)+"@cluster0.ebzle64.mongodb.net/"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# mydb = client["crossword-solver"]
# mycol = mydb["puzzles_images"]
# puzzles = mydb["puzzles"]



# for i in range(9093,16757):
#     data = puzzles.find_one({"number": i })
#     if data:
#         with open('../static/puzzles/svgs/9093.svg', 'rb') as file:
#             svg_data = file.read()

#         # Convert the SVG data to a BSON binary object
#         svg_blob = Binary(svg_data)
#         mycol.insert_one({"number": i, "svg": svg_blob})
#         print(f"Inserted SVG for puzzle {i}")
#     else:
#         print(f"Skipping puzzle {i}")

    







import base64



def png_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        # Read the binary image data
        binary_data = image_file.read()
        # Encode binary data to Base64
        base64_data = base64.b64encode(binary_data).decode("utf-8")
        print(base64_data)
        return base64_data
    


base64_data = png_to_base64("../static/puzzles/svgs/png/9093.png") 

print(base64_data)