from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:proiectip@cluster0-cirwn.mongodb.net/test?retryWrites=true&w=majority")
db = client['proiectip']

restaurantsCollection = db['restaurants']
