from pymongo import MongoClient

uri = "mongodb+srv://sarithasankari154_db_user:LYN9jIbrcmPIPaGM@cluster0.dvbj5qg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    print("✅ Connected Successfully")
except Exception as e:
    print("❌ Error:", e)