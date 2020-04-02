from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:proiectip@cluster0-cirwn.mongodb.net/test?retryWrites=true&w=majority")
db = client['proiectip']


def clear_collection(name):
    collection = db[name]
    print(collection.delete_many({}).deleted_count)

def clear_all():
    clear_collection("restaurants")
    clear_collection("reviews")
    clear_collection("customers")
