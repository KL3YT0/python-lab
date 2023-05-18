from math import sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np


def is_not_tolerance(x):
    return not (-9 <= x <= 5)


def func1(x):
    return -((-x - 5) * (x + 9)) ** (0.5) + 2


def func2(x):
    return 2


def func3(x):
    return -0.5 * x


def func4(x):
    return sin(x)


def func5(x):
    return x - pi


def piecewise_func(x):
    if -9 <= x < -5:
        return func1(x)
    if -5 <= x < -4:
        return func2(x)
    if -4 <= x < 0:
        return func3(x)
    if 0 <= x < pi:
        return func4(x)
    if pi <= x <= 5:
        return func5(x)
    raise Exception('{0} ∉ [-9, 5]'.format(x))


def draw_table(x_grid, y_grid):
    print("+--------+--------+")
    print("I   X    I    Y   I")
    print("+--------+--------+")

    for i in range(len(x_grid)):
        print("I{0: 7.2f} I{1: 7.2f} I".format(x_grid[i], y_grid[i]))


data = []
x_grid = np.arange(-9, 5.5, 0.5)
y_grid = []

for x in x_grid:
    y_grid.append(piecewise_func(x))

draw_table(x_grid, y_grid)
