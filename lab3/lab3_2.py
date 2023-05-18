from math import sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np


def exp(x, eps):
    sum = 1
    last_el = 1
    n = 1

    while (abs(last_el) > eps):
        curr_el = last_el * x / n
        sum += curr_el
        last_el = curr_el
        n += 1

    return [sum, n]


def draw_table(x, y, n):
    print("+-------------+-------------+-------------+")
    print("I     X       I      Y      I       N     I")
    print("+-------------+-------------+-------------+")

    for i in range(len(x)):
        print("I{0: 12.2f} I{1: 12.2f} I{2: 12.2f} I".format(x[i], y[i], n[i]))

    print("+-------------+-------------+-------------+")


print('Type x_0 x_n dx x eps, for example: 0 3 0.01 2 0.01')
input_value = input()
params = input_value.split(' ')
params = [float(param) for param in params]
x_0, x_n, dx, x, eps = params

x_grid = np.arange(x_0, x_n, dx)
y_grid = np.array([])
n_grid = np.array([])
N = len(x_grid)

for x in x_grid:
    curr_y, curr_n = exp(x, eps)
    y_grid = np.append(y_grid, curr_y)
    n_grid = np.append(n_grid, curr_n)

print('x_0 = {0}, x_n = {1}, dx = {2}, eps = {3}'.format(x_0, x_n, dx, eps))

draw_table(x_grid, y_grid, n_grid)
