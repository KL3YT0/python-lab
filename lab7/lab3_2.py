from math import sin, cos, pi
import random
import matplotlib.pyplot as plt
import numpy as np


def monte_carlo_method(steps):
    favorable = 0

    random.seed()
    for step in range(steps):
        x = random.uniform(x_start, x_end)
        y = random.uniform(y_start, y_end)

        if (point_in_area(x, y)):
            favorable += 1
            add_point_to_graph(x, y, True)

        else:
            add_point_to_graph(x, y, False)

    return favorable / steps * full_area


def first_upper_func(x):
    return 50 - (2500 - (x + 50) * (x + 50)) ** (0.5)


def second_upper_func(x):
    return 50


def first_lower_func(x):
    return -50


def second_lower_func(x):
    return -50 + (2500 - (x - 50) * (x - 50)) ** (0.5)


def piecewise_upper_func(x):
    if (x_start <= x < 0):
        return first_upper_func(x)

    if (0 <= x <= x_end):
        return second_upper_func(x)

    raise Exception('{0} ∉ [{1}, {2}]'.format(x, x_start, x_end))


def piecewise_lower_func(x):
    if (x_start <= x < 0):
        return first_lower_func(x)

    if (0 <= x <= x_end):
        return second_lower_func(x)

    raise Exception('{0} ∉ [{1}, {2}]'.format(x, x_start, x_end))


def point_in_area(x, y):
    return piecewise_lower_func(x) <= y <= piecewise_upper_func(x)


def add_point_to_graph(x, y, favorable):
    if (favorable):
        plt.scatter(x, y, color='green', s=10, marker='o')
    else:
        plt.scatter(x, y, color='red', s=10, marker='o')


def add_graph():
    x_grid_upper = np.arange(x_start, x_end, 0.01)
    y_grid_upper = [piecewise_upper_func(x) for x in x_grid_upper]
    y_grid_upper = np.array(y_grid_upper)

    x_grid_lower = np.arange(x_start, x_end, 0.01)
    y_grid_lower = [piecewise_lower_func(x) for x in x_grid_lower]
    y_grid_lower = np.array(y_grid_lower)

    plt.plot(x_grid_upper, y_grid_upper)
    plt.plot(x_grid_lower, y_grid_lower)

    plt.xlim(-125, 100)

    plt.grid(True)


full_area = 10000
real_filled_area = 6073.00918301
x_start = -50
x_end = 50

y_start = -50
y_end = 50

x = 25
y = -10

# print('point ({0}, {1}) in area: '.format(x, y), point_in_area(x, y))

calc_filled_area = monte_carlo_method(100)

print('calc_filled_area', calc_filled_area)

if (calc_filled_area > real_filled_area):
    print('currency', real_filled_area / calc_filled_area * 100)

else:
    print('currency', calc_filled_area / real_filled_area * 100)

add_graph()

plt.show()
