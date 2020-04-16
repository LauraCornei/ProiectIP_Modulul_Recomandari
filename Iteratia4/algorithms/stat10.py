import matplotlib.pyplot as plt

# http://127.0.0.1:5000/recommendations/stats/customers_per_hours


def get_hour_of(order):
    digit1 = order['order_date'][11:12]
    digit2 = order['order_date'][12:13]
    digit1 = int(digit1)
    digit2 = int(digit2)
    ind = digit1*10+digit2
    return ind


def get_min_of(order):
    digit1 = order['order_date'][11:12]
    digit2 = order['order_date'][12:13]
    digit1 = int(digit1)
    digit2 = int(digit2)

    digit1_m = order['order_date'][14:15]
    digit2_m = order['order_date'][15:16]
    digit1_m = int(digit1_m)
    digit2_m = int(digit2_m)

    ind = (digit1*10+digit2)*60+(digit1_m*10+digit2_m)
    return ind


def calc_no_orders_hours(orders):
    no_orders = [0] * 24
    for order in orders:
        ind = get_hour_of(order)
        no_orders[ind] += 1
    return no_orders


def calc_no_orders_min(orders):
    no_orders = [0] * 24 * 60
    for order in orders:
        ind = get_min_of(order)
        no_orders[ind] += 1
    return no_orders


def calc_no_orders_half_hours(orders):
    no_orders = [0] * 24 * 2
    for order in orders:
        ind = int(get_min_of(order)/30)
        no_orders[ind] += 1
    return no_orders


def main_hours(orders):
    fig, ax = plt.subplots()
    hours = [0] * 24
    for ind in range(0, 24):
        hours[ind] = ind

    no_orders = calc_no_orders_hours(orders)

    ax.plot(hours, no_orders)
    ax.set(xlabel='Time of order (hours)', ylabel='No of customers ', title='Customers per hours')
    ax.grid()
    return fig


def main_half_hours(orders):

    fig, ax = plt.subplots()
    half_hours = [0] * 24 * 2
    for ind in range(0, 48):
        half_hours[ind] = ind

    no_orders = calc_no_orders_half_hours(orders)

    ax.plot(half_hours, no_orders)
    ax.set(xlabel='Time of order (30 min)', ylabel='No of customers ', title='Customers per hours')
    ax.grid()
    return fig


def main_min(orders):
    fig, ax = plt.subplots()
    min = [0] * 24 * 60
    for ind in range(0, 60):
        min[ind] = ind

    no_orders = calc_no_orders_min(orders)

    ax.plot(min, no_orders)
    ax.set(xlabel='Time of order (min)', ylabel='No of customers ', title='Customers per hours')
    ax.grid()
    return fig

