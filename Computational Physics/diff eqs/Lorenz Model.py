import numpy as np


def lorenz(x, t, s=10, r=28, b=2.667):
    return np.array([s * (x[1] - x[0]), r * x[0] - x[1] - x[0] * x[2], x[0] * x[1] - b * x[2]])


def rk4_lorenz(x0, t):
    x = np.empty((len(t), 3))
    x[0] = x0
    for i in range(1, len(t)):
        h = t[i] - t[i - 1]
        k1 = h * lorenz(x[i - 1], t[i - 1])
        k2 = h * lorenz(x[i - 1] + k1 / 2, t[i - 1] + h / 2)
        k3 = h * lorenz(x[i - 1] + k2 / 2, t[i - 1] + h / 2)
        k4 = h * lorenz(x[i - 1] + k3, t[i - 1] + h)
        x[i] = x[i - 1] + k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6
    return x


x0 = np.array([8.0, 0.0, 30.0])
t = np.linspace(0, 100, 10000)
x = rk4_lorenz(x0, t)

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x[:, 0], x[:, 1], x[:, 2], lw=0.5)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
plt.show()
