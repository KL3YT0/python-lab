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


def draw_graph():
    data = []
    x = np.arange(-9, 5, 0.1)
    y = []

    for a in x:
        y.append(piecewise_func(a))

    plt.plot(x, y)
    plt.show()


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


draw_graph()

x = float(input('Type x ∈ [-9, 5]: '))

if is_not_tolerance(x):
    print('{0} is not tolerance value'.format(x))
    exit()

print('f({0}) = {1}'.format(x, piecewise_func(x)))
