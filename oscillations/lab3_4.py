import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

w_0 = 0.4
x_0 = 2
v_0 = 3
eps = 0.1
eps1 = 2.0

def f(Y, t):
    x, y = Y
    return [y, eps*(1 - x**2)*y - x]
def fvdp1(t,y):
    dy1 = y [1]
    dy2 = eps*(1 - y[0]**2)*y[1] - y[0]
    return [dy1,dy2]

"""def solve_second_order_ode():
    global eps
    t2 = np.linspace(0,20,1000)
    y0 = [x_0, v_0]
    y = odeint(fvdp1, y0, t2, tfirst=True)
    plt.figure(2, figsize=(15, 9))
    plt.subplot(221)
    plt.title("$ \epsilon = $" + str(eps), loc='left')
    y1, = plt.plot(t2,y[:,0],label='x')
    plt.xlabel('$t$')
    plt.ylabel('$x(t)$')
    plt.grid()
    plt.legend(handles=[y1])
    plt.subplot(222)
    y1_1, = plt.plot(t2,y[:,1],label='x‘')
    plt.legend(handles=[y1_1])
    plt.xlabel('$t$')
    plt.ylabel('$x‘(t)$')
    plt.grid()

    eps = 5.0
    y0 = [x_0, v_0]
    y = odeint(fvdp1, y0, t2, tfirst=True)
    plt.subplot(223)
    plt.title("$\epsilon = $" + str(eps), loc='left')
    y1, = plt.plot(t2,y[:,0],label='x')
    plt.xlabel('$t$')
    plt.ylabel('$x(t)$')
    plt.legend(handles=[y1])
    plt.grid()
    plt.subplot(224)
    y1_1, = plt.plot(t2,y[:,1],label='x‘')
    plt.legend(handles=[y1_1])
    plt.xlabel('$t$')
    plt.ylabel('$x‘(t)$')
    plt.grid()
"""
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
t=0
X, Y = np.meshgrid(x, y)
u, v = np.zeros(X.shape), np.zeros(Y.shape)
NI, NJ = X.shape
for i in range(NI):
    for j in range(NJ):
         x = X[i, j]
         y = Y[i, j]
         values = f([x, y], t)
         u[i,j] = values[0]
         v[i,j] = values[1]
epsh = eps

#solve_second_order_ode()

plt.figure(1, figsize=(15, 5))
plt.subplot(121)
plt.title("$\epsilon = $" + str(epsh))
plt.streamplot(X, Y, u, v)
plt.xlabel('$x$')
plt.ylabel('$dx/dt$')
plt.grid()
plt.subplot(122)
eps = eps1
for i in range(NI):
    for j in range(NJ):
         x = X[i, j]
         y = Y[i, j]
         values = f([x, y], t)
         u[i,j] = values[0]
         v[i,j] = values[1]
plt.streamplot(X, Y, u, v)
plt.title("$\epsilon = $" + str(eps1))
plt.xlabel('$x$')
plt.ylabel('$dx/dt$')
plt.grid()
plt.show()
