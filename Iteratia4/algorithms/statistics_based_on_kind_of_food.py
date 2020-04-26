
# http://127.0.0.1:5000/recommendations/stats/food_per_restaurant/5e958949564a0055b294ce83/desc/false/-1


def create_barh_plot(food_label, quantity):
    import numpy as np
    import matplotlib.pyplot as plt

    x = food_label
    y = quantity
    color_1 = "#a71d31"  # red
    color_2 = "#386150"  # green
    color_3 = "#2b2633"  # black
    color_4 = "#453d52"  # light-black

    fig, ax = plt.subplots(figsize=(14, 8))
    plt.title('Food per restaurant statistic', fontsize=18, fontweight='bold')

    width = 0.85
    ind = np.arange(len(y))

    ax.barh(ind, y, width, color=[color_1, color_2, color_3], alpha=0.95)
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels(x, minor=False)

    for i, v in enumerate(y):
        ax.text(v + 0.02, i - 0.08, str(v), color='black', fontweight='bold')

    for i, v in enumerate(x):
        ax.text(0.2, i - 0.08, v, color='white', fontweight='bold')

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(axis='x', colors=color_4, labelsize=8)
    ax.set_yticks([])
    ax.margins(0, 0.02)
    ax.grid(which='major', axis='x', linestyle='dashed')
    ax.set_axisbelow(True)
    plt.box(False)
    return fig


def get_statistics_per_restaurant(restaurant_id, foods, orders, sort_order, show_count):
    food_name_by_id = {}
    food_dict = {}
    tick_label = []
    height = []
    for food in foods:
        if restaurant_id == 0 or food["restaurant_id"] == restaurant_id:
            food_dict[food["name"]] = 0
            food_name_by_id[food["_id"]] = food["name"]

    for order in orders:
        if restaurant_id == 0 or order["restaurant_id"] == restaurant_id:
            food_dict[food_name_by_id[order["food_id"]]] += 1

    sorted_food_dict = {}
    if sort_order == "asc":
        sorted_food_dict = sorted(food_dict.items(), key=lambda kv: kv[1])
    elif sort_order == "desc":
        sorted_food_dict = sorted(food_dict.items(), key=lambda kv: kv[1], reverse=True)

    if show_count == -1:
        print_count = 20
    else:
        print_count = show_count

    for food in sorted_food_dict:
        tick_label.append(food[0])
        height.append(food[1])
        print_count -= 1
        if print_count == 0:
            break

    return create_barh_plot(tick_label, height)



