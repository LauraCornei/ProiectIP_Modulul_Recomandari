from models.Customers import Customers
from models.Reviews import Reviews
from models.Foods import Foods
from models.Restaurants import Restaurant


def get_fav_res(customer, reviews):

    max_review = -1
    fav_res = -1
    for review in reviews:
        if review["customer_id"] == customer["_id"] and review["score"] > max_review:
            max_review = review["score"]
            fav_res = review["restaurant_id"]

    return fav_res


def get_cluster(reviews, fav_res):

    cluster = []
    for review in reviews:
        if review["restaurant_id"] == fav_res and review["score"] > 3.5:
            cluster.append(review["customer_id"])
    return cluster


def restaurant_top(reviews, fav_res):

    cluster = get_cluster(reviews, fav_res)
    restaurants = []
    for customer_id in cluster:
        for review in reviews:
            if review["customer_id"] == customer_id and review["score"] > 3.5 and review["restaurant_id"] != fav_res:
                restaurants.append(review["restaurant_id"])
    return restaurants


def score_mean(reviews, res):
    score_dic = dict.fromkeys(res, 0)
    count_dic = dict.fromkeys(res, 0)
    for review in reviews:
        if res.count(review["restaurant_id"]):
            score_dic[review["restaurant_id"]] += review["score"]
            count_dic[review["restaurant_id"]] += 1

    mean_dic = dict.fromkeys(res)
    for r in res:
        mean_dic[r] = score_dic[r]/count_dic[r]

    return mean_dic


def filter_res(customer, reviews, foods):
    fav_res = get_fav_res(customer, reviews)
    res_top = restaurant_top(reviews, fav_res)
    filtered_res = []
    menu_fav = []
    for food in foods:
        if food["restaurant_id"] == fav_res:
            menu_fav.append(food["name"])

    for food in foods:
        if menu_fav.count(food["name"]) and res_top.count(food["restaurant_id"]):
            filtered_res.append(food["restaurant_id"])

    res_dic = score_mean(reviews, list(set(filtered_res)))
    sorted_top = sorted(res_dic, key=lambda item: res_dic[item], reverse=True)
    for s in sorted_top:
        print(res_dic[s])
    return sorted_top[0:9]


result = filter_res(Customers.by_id('5e8d959a9220ac402a589b57'), Reviews.all(), Foods.all())

for r in result:
    print(Restaurant.by_id(r))
