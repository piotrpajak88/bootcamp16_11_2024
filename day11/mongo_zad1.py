import pymongo

# connect to MongoDB, change 'localhost' and '27017' to your MongoDB server's IP and port
# change 'localhost' and '27017' to your MongoDB server's
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

print(mydb.list_collection_names())

