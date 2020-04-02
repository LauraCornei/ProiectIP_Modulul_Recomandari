from pymongo import MongoClient
import json
import random as rnd
from Misc import clearDataBase

client = MongoClient("mongodb+srv://test:proiectip@cluster0-cirwn.mongodb.net/test?retryWrites=true&w=majority")
db = client['proiectip']


def add_customers():
    clearDataBase.clear_collection("customers")
    customers = db["customers"]

    with open('customers.json') as json_file:
        data = json.load(json_file)
        customers.insert_many(data)
        print(customers.count({}))


def add_restaurants():
    clearDataBase.clear_collection("restaurants")
    restaurants = db["restaurants"]

    with open('restaurants.json') as json_file:
        data = json.load(json_file)
        restaurants.insert_many(data)
        print(restaurants.count({}))


def add_reviews():
    clearDataBase.clear_collection("reviews")
    REVIEWS_PER_CUSTOMERS = 5
    rnd.seed(324324)
    restaurants = list(db["restaurants"].find())
    customers = list(db["customers"].find())
    reviews_data = []
    reviews = db["reviews"]

    restaurants_count = len(restaurants)
    for customer in customers:
        for i in range(0, REVIEWS_PER_CUSTOMERS):
            restaurant = restaurants[rnd.randint(0, restaurants_count - 1)]
            review = dict()
            review["restaurant_id"] = restaurant["_id"]
            review["customer_id"] = customer["_id"]
            review["score"] = rnd.randint(1, 5)
            reviews_data.append(review)
    reviews.insert_many(reviews_data)


add_restaurants()
add_customers()
add_reviews()
