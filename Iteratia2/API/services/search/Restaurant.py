from models.Restaurant import Restaurant
from bson.json_util import dumps
def main():
    return dumps(Restaurant.all())