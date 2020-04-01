from services.recommendation import Food, Restaurant
from flask_classful import FlaskView

class RecommendationController(FlaskView):
    def restaurant(self):
        return Restaurant.main()
    def food(self):
        return Food.main()

