from math import exp, cos
import numpy as np
import matplotlib.pyplot as plt


def fx(x, y):
    return np.exp(x + 2 * y) - np.cos(3 * x)


def fy(x, y):
    return (4 + 8 * x) ** (0.5) - 2 * np.exp(y)


def fx1(x, y):
    return 4 - 4 * x - 2 * y


def fy1(x, y):
    return x * y


def fx2(x, y):
    return y


def fy2(x, y):
    return -3*x-4*y


Y, X = np.mgrid[-3:3:1400j, -3:3:1400j]
U = fx1(X, Y)
V = fy1(X, Y)
plt.streamplot(X, Y, U, V, density=1)
plt.grid()
plt.legend()

plt.show()
