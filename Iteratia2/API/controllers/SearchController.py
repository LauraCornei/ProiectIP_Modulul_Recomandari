from services.search import Restaurant, Food
from flask_classful import FlaskView, route

class SearchController(FlaskView):
    def restaurant(self):
        return Restaurant.main()
    def food(self):
        return Food.main()