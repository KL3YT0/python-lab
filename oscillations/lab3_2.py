import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sy
from scipy.integrate import odeint

w_0 = 0.4
fi_0 = math.pi / 6.0
fi_1 = math.pi / 2.0
v_0 = 0.5

def f(Y, t):
    x, y = Y
    return [y, -w_0 ** 2 * math.sin(x)]

def fode1(t, y):
    dy1 = y[1]
    dy2 = - w_0 ** 2 * math.sin(y[0])
    return [dy1, dy2]

def fode2(t, y):
    dy1 = y[1]
    dy2 = - w_0 ** 2 * y[0]
    return [dy1, dy2]

def plot_graphs():
    t2 = np.linspace(0, 100, 10000)
    y0 = [fi_0, v_0]
    y = odeint(fode1, y0, t2, tfirst=True)
    y_1 = odeint(fode2, y0, t2, tfirst=True)

    plt.figure(2, figsize=(15, 9))
    plt.subplot(221)
    plt.title("$\phi_0 = {:.3f}$ радиан".format(fi_0), loc='left')
    y1, = plt.plot(t2, y[:, 0], label='x - с синусом')
    y2, = plt.plot(t2, y_1[:, 0], label='x - без синуса ')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.grid()

    plt.legend(handles=[y1, y2])
    plt.subplot(222)
    y1_1, = plt.plot(t2, y[:, 1], label='x‘')
    y1_2, = plt.plot(t2, y_1[:, 1], label='x‘')
    plt.legend(handles=[y1_1, y1_2])
    plt.xlabel('t')
    plt.ylabel('x‘(t)')
    plt.grid()

    y0 = [fi_1, v_0]
    y = odeint(fode1, y0, t2, tfirst=True)
    y_1 = odeint(fode2, y0, t2, tfirst=True)

    plt.subplot(223)
    plt.title("$\phi_0 = {:.3f}$ радиан".format(fi_1), loc='left')
    y1, = plt.plot(t2, y[:, 0], label='x - с синусом')
    y2, = plt.plot(t2, y_1[:, 0], label='x - без синуса ')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.grid()

    plt.legend(handles=[y1, y2])
    plt.subplot(224)
    y1_1, = plt.plot(t2, y[:, 1], label='x‘')
    y1_2, = plt.plot(t2, y_1[:, 1], label='x‘')
    plt.legend(handles=[y1_1, y1_2])
    plt.xlabel('t')
    plt.ylabel('x‘(t)')
    plt.grid()
    plt.show()

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
t = 0
X, Y = np.meshgrid(x, y)
u, v = np.zeros(X.shape), np.zeros(Y.shape)
NI, NJ = X.shape
for i in range(NI):
    for j in range(NJ):
        x = X[i, j]
        y = Y[i, j]
        values = f([x, y], t)
        u[i, j] = values[0]
        v[i, j] = values[1]
plt.figure(1, figsize=(5, 5))
plt.title('Ангармонический осциллятор')
plt.streamplot(X, Y, u, v)
plt.xlabel('x')
plt.ylabel('dx/dt')
plt.grid()

plot_graphs()

