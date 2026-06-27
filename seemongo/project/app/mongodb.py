from pymongo import MongoClient
import certifi

client=MongoClient("mongodb+srv://sarithasankari154_db_user:LYN9jIbrcmPIPaGM@cluster0.dvbj5qg.mongodb.net/?appName=Cluster0",
                   tlsCAFile=certifi.where()

)
db=client["StudentDB11"]
user_collection=db["users"]