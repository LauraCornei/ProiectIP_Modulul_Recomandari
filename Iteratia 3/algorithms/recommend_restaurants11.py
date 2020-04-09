from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:proiectip@cluster0-cirwn.mongodb.net/test?retryWrites=true&w=majority")
db = client['proiectip']


def get_food_by_id(food_id, foods):
    for food in foods:
        if food['_id'] == food_id:
            return food
    return -1


# returneaza o lista cu numele mancarurilor disponibile la restaurant
def get_restaurant_menu(restaurant, foods):
    menu = []
    for food in foods:
        if food['restaurant_id'] == restaurant['_id']:
            menu.append(food['name'])
    return menu


# returneaza un dictionar cu numele si de cate ori a fost comandata de catre customer fiecare fel de mancare
# care nu apare in meniul restaurantului
def get_customer_other_foods(customer_id, orders, foods, restaurant_menu):
    customer_other_foods = {}
    for order in orders:
        if order['customer_id'] == customer_id:
            food = get_food_by_id(order['food_id'], foods)
            if food['name'] not in restaurant_menu:
                if food['name'] not in customer_other_foods:
                    customer_other_foods[food['name']] = 1
                else:
                    customer_other_foods[food['name']] += 1
    return customer_other_foods


# returneaza un dictionar cu perechi customer_id - numar de comenzi la restaurant
def get_restaurant_clients(restaurant, orders):
    clients = {}
    for order in orders:
        if order['restaurant_id'] == restaurant['_id']:
            if order['customer_id'] not in clients:
                clients[order['customer_id']] = 1
            else:
                clients[order['customer_id']] += 1
    return clients


def final(restaurant, orders, foods):
    # orders_collection = db['orders']
    # orders = list(orders_collection.find())
    # foods_collection = db['foods']
    # foods = list(foods_collection.find())
    recommendations = {}
    clients = get_restaurant_clients(restaurant, orders)
    restaurant_menu = get_restaurant_menu(restaurant, foods)
    for customer_id in clients:
        customer_other_foods = get_customer_other_foods(customer_id, orders, foods, restaurant_menu)
        for food in customer_other_foods:
            if food not in recommendations:
                recommendations[food] = 1 + 0.2 * customer_other_foods[food] * clients[customer_id]
            else:
                recommendations[food] = 1 + 0.2 * customer_other_foods[food] * clients[customer_id]

    result = {k: v for k, v in sorted(recommendations.items(), key=lambda item: item[1], reverse=True)}
    return list(result.keys())[:10]
    # return recommendations


restaurantsCollection = db['restaurants']
restaurants = list(restaurantsCollection.find())
orders_collection = db['orders']
orders = list(orders_collection.find())
foods_collection = db['foods']
foods = list(foods_collection.find())
print(final(restaurants[0],orders,foods))
