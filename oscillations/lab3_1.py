import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

w_0 = 0.3
fi_0 = np.math.pi * 0
# для затухания
b = 0.03
# для вынуждающей силы
f_0 = 2
v_0 = 0.45


def f(Y, t):
    x, y = Y
    return [y, -w_0 ** 2 * x]


def fode(t, y):
    dy1 = y[1]
    dy2 = -w_0 ** 2 * y[0]
    return [dy1, dy2]


def f2(Y, t):
    x, y = Y
    return [y, -2*b*y-w_0**2*x]


def fode2(t, y):
    dy1 = y[1]
    dy2 = -2*b*y[1]-w_0**2*y[0]
    return [dy1, dy2]


def f3(Y, t):
    x, y = Y
    return [y, f_0*np.math.cos(v_0*t)-w_0**2*x]


def fode3(t, y):
    dy1 = y[1]
    dy2 = f_0*np.math.cos(v_0*t)-w_0**2*y[0]
    return [dy1, dy2]


def plot_graphs():
    t2 = np.linspace(0, 100, 10000)
    y0 = [fi_0, v_0]
    y = odeint(fode, y0, t2, tfirst=True)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].plot(t2, y[:, 0], label='x')
    axes[0].set_xlabel('t')
    axes[0].set_ylabel('x(t)')
    axes[0].grid()
    axes[1].plot(t2, y[:, 1], label='x‘')
    axes[1].set_title('Уравнение гармонического осциллятора')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('x‘(t)')
    axes[1].grid()
    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
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
    axes[2].streamplot(X, Y, u, v)
    axes[2].set_xlabel('x')
    axes[2].set_ylabel('x‘(t)')
    axes[2].grid()

    # Второе задание
    t2 = np.linspace(0, 100, 10000)
    y0 = [fi_0, v_0]
    y = odeint(fode2, y0, t2, tfirst=True)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].plot(t2, y[:, 0], label='x')
    axes[0].set_xlabel('t')
    axes[0].set_ylabel('x(t)')
    axes[0].grid()
    axes[1].plot(t2, y[:, 1], label='x‘')
    axes[1].set_title('Уравнение гармонического осциллятора с затуханием')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('x‘(t)')
    axes[1].grid()
    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
    t = 0
    X, Y = np.meshgrid(x, y)
    u, v = np.zeros(X.shape), np.zeros(Y.shape)
    NI, NJ = X.shape
    for i in range(NI):
        for j in range(NJ):
            x = X[i, j]
            y = Y[i, j]
            values = f2([x, y], t)
            u[i, j] = values[0]
            v[i, j] = values[1]
    axes[2].streamplot(X, Y, u, v)
    axes[2].set_xlabel('x')
    axes[2].set_ylabel('x‘(t)')
    axes[2].grid()

    # Третье задание
    t2 = np.linspace(0, 100, 10000)
    y0 = [fi_0, v_0]
    y = odeint(fode3, y0, t2, tfirst=True)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].plot(t2, y[:, 0], label='x')
    axes[0].set_xlabel('t')
    axes[0].set_ylabel('x(t)')
    axes[0].grid()
    axes[1].plot(t2, y[:, 1], label='x‘')
    axes[1].set_title(
        'Уравнение гармонического осциллятора с вынуждающей силой')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('x‘(t)')
    axes[1].grid()
    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
    t = 0
    X, Y = np.meshgrid(x, y)
    u, v = np.zeros(X.shape), np.zeros(Y.shape)
    NI, NJ = X.shape
    for i in range(NI):
        for j in range(NJ):
            x = X[i, j]
            y = Y[i, j]
            values = f3([x, y], t)
            u[i, j] = values[0]
            v[i, j] = values[1]
    axes[2].streamplot(X, Y, u, v)
    axes[2].set_xlabel('x')
    axes[2].set_ylabel('x‘(t)')
    axes[2].grid()

    plt.show()


plot_graphs()
