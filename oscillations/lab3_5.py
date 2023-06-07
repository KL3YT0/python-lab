import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

w_0 = 0.4
x_0 = 2
v_0 = 0.35
eps = 0.05
b = 0.0

def w(t):
    return w_0**2*(1 - eps*math.cos(2*w_0*t))
def w1(t):
    return math.cos(w_0*t)

#для интересного случая
def f(Y, t):
    x, y = Y
    return [y, -2*b*y - w(t)*x]
#для варианта
def f1(Y, t):
    x, y = Y
    return [y, -2*b*y - w1(t)*x]

def fvdp1(t,y):
    dy1 = y [1]
    dy2 = -2*b*y[1] - w(t)*y[0]
    return [dy1,dy2]

def fvdp2(t,y):
    dy1 = y [1]
    dy2 = -2*b*y[1] - w1(t)*y[0]
    return [dy1,dy2]

def solve_second_order_ode():
    t2 = np.linspace(0,500,2000)
    y0 = [x_0, v_0]
    y = odeint(fvdp1, y0, t2, tfirst=True)

    plt.figure(2, figsize=(15, 9))
    plt.subplot(221)
    plt.title("$ w(t) = w^2_0 (1 - \epsilon cos(2w_0t)$",loc='left')
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

    y0 = [x_0, v_0]
    y = odeint(fvdp2, y0, t2, tfirst=True)
    plt.subplot(223)
    plt.title("$w(t) = cos(w_0t)$", loc='left')
    y1, = plt.plot(t2,y[:,0],label='x')
    plt.xlabel('$t$')
    plt.ylabel('$x(t)$')
    plt.grid()

    plt.legend(handles=[y1])
    plt.subplot(224)
    y1_1, = plt.plot(t2,y[:,1],label='x‘')
    plt.legend(handles=[y1_1])
    plt.xlabel('$t$')
    plt.ylabel('$x‘(t)$')
    plt.grid()
    plt.show()

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
plt.figure(1, figsize=(15, 5))
plt.subplot(121)
plt.title("$w(t) = w^2_0 (1 - \epsilon cos(2w_0t)$")
plt.streamplot(X, Y, u, v)
plt.xlabel('$x$')
plt.ylabel('$dx/dt$')
plt.grid()

plt.subplot(122)
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
         values = f1([x, y], t)
         u[i,j] = values[0]
         v[i,j] = values[1]
plt.streamplot(X, Y, u, v)
plt.title("$w(t) = cos(w_0t)$")
plt.xlabel('$x$')
plt.ylabel('$dx/dt$')
plt.grid()
plt.show()
solve_second_order_ode()