from pymongo import MongoClient
import certifi

client = MongoClient(
    "mongodb+srv://sarithasankari154_db_user:LYN9jIbrcmPIPaGM@cluster0.dvbj5qg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    tlsCAFile=certifi.where()
)

db = client["StudentDB"]

users_collection = db["users"]