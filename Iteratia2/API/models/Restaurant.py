from db import restaurantsCollection


class Restaurant(object):
    @staticmethod
    def all():
        return restaurantsCollection.find()
