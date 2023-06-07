import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

w_0 = 0.4
x_0 = 1
x_1 = 3.0
v_0 = 1.5
k = 1.0
m = 1.0
k1 = 1.0


def f(Y, t):
    x, y = Y
    return [y, -(k/m)*(x + (k1/k)*x**3)]

def fode1(t,y):
    dy1 = y [1]
    dy2 = -(k/m)*(y[0] + (k1/k)*y[0]**3)
    return [dy1,dy2]
'''

def f(Y, t):
    x, y = Y
    return [y, -(k/m)*x]

def fode1(t,y):
    dy1 = y [1]
    dy2 = -(k/m)*y[0]
    return [dy1,dy2]
'''
def plot_graphs():
     global k1
     t2 = np.linspace(0,20,1000)
     y0 = [x_0, v_0]
     y = odeint(fode1, y0, t2, tfirst=True)

     y0 = [x_1, v_0]
     y_1 = odeint(fode1, y0, t2, tfirst=True)

     plt.figure(2, figsize=(15, 5))
     plt.subplot(121)
     tit1 = "$ x_0 = $" + str(x_0)
     tit2 = "$ x_0 = $" + str(x_1)
     y1, = plt.plot(t2,y[:,0], label=tit1)
     y2, = plt.plot(t2,y_1[:,0],label=tit2)
     plt.legend(handles=[y1, y2])
     plt.xlabel('$t$')
     plt.ylabel('$x(t)$')
     plt.grid()

     plt.subplot(122)
     y1_1, = plt.plot(t2,y[:,1],label="x‘")
     y2_1, = plt.plot(t2,y_1[:,1],label="x‘")
     plt.legend(handles=[y1_1, y2_1])
     plt.xlabel('$t$')
     plt.ylabel('$x‘(t)$')
     plt.grid()
     plt.show()

x = np.linspace(-2.5, 2.5, 1000)
y = np.linspace(-1.5, 1.5, 1000)
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
plt.figure(1, figsize=(5, 5))
plt.streamplot(X, Y, u, v)
plt.xlabel('$x$')
plt.ylabel('$dx/dt$')
plt.grid()

plot_graphs()