# from pymongo import MongoClient
#
# client = MongoClient("mongodb+srv://test:proiectip@cluster0-cirwn.mongodb.net/test?retryWrites=true&w=majority")
# db = client['proiectip']

NUMBER_OF_CUSTOMERS = 10
NUMBER_OF_FOODS = 10


def filter_orders(orders, restaurant_id):
    restaurant_orders = []
    for order in orders:
        if order['restaurant_id'] == restaurant_id:
            restaurant_orders.append(order)
    return restaurant_orders


def get_customer_food_dict(customer_id, orders):
    customer_foods = {}
    for order in orders:
        if order['customer_id'] == customer_id:
            if order['food_id'] not in customer_foods:
                customer_foods[order['food_id']] = 1
            else:
                customer_foods[order['food_id']] += 1
    return customer_foods


def get_similarity(customer_dict1, customer_dict2):
    score = 0
    for food_id in customer_dict1:
        if food_id in customer_dict2:
            score += (customer_dict1[food_id] + customer_dict2[food_id]) / 2
    return score


def get_recommended_foods(similar_customers_foods, similar_customers_ordered):
    food_dict = {}
    for customer_id in similar_customers_foods:
        for food_id in similar_customers_foods[customer_id]:
            if food_id not in food_dict:
                food_dict[food_id] = similar_customers_foods[customer_id][food_id] * similar_customers_ordered[
                    customer_id]
            else:
                food_dict[food_id] += similar_customers_foods[customer_id][food_id] * similar_customers_ordered[
                    customer_id]
    recommended_foods = {k: v for k, v in
                         sorted(food_dict.items(), key=lambda item: item[1], reverse=True)}
    recommended_foods_ids = list(recommended_foods.keys())[:10]
    if len(recommended_foods_ids) < 10:
        return recommended_foods_ids
    else:
        return recommended_foods_ids[:10]


"""
   pt similaritatea intre 2 customeri:
       1: cate feluri comune de mancare apar intre 2 dicitonare pt customer (chei)
       2: data ultimei comenzi
       3: pretu
       4: frecventa
   """


def final(customer_id, restaurant_id, orders):
    restaurant_orders = filter_orders(orders, restaurant_id)
    # original_customer_foods = get_customer_food_dict(customer_id, restaurant_id, restaurant_orders)
    customers_orders = {}
    for order in restaurant_orders:
        if order['customer_id'] not in customers_orders:
            customers_orders[order['customer_id']] = get_customer_food_dict(order['customer_id'],
                                                                            restaurant_orders)
    customers_similarities = {}
    for customer2_id in customers_orders:
        customers_similarities[customer2_id] = get_similarity(customers_orders[customer_id],
                                                              customers_orders[customer2_id])

    similar_customers_ordered = {k: v for k, v in
                                 sorted(customers_similarities.items(), key=lambda item: item[1], reverse=True)}
    first_similar_customers = list(similar_customers_ordered.items())[:NUMBER_OF_CUSTOMERS]
    similar_customers_foods = {}
    for customer_id in first_similar_customers:
        similar_customers_foods[customer_id[0]] = customers_orders[customer_id[0]]

    return get_recommended_foods(similar_customers_foods, similar_customers_ordered)

# orders_collection = db['orders']
# orders = list(orders_collection.find())
# restaurantsCollection = db['restaurants']
# restaurants = list(restaurantsCollection.find())
# customersCollection = db['customers']
# customers = list(customersCollection.find())
#
# recommended_foods = final(customers[0]['_id'], restaurants[0]['_id'], orders)
# print(recommended_foods)
