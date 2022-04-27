import numpy as np
from matplotlib import pyplot as plt
from numpy import sqrt, square, cos

phi = 0
k = 1
m = 1
w = sqrt(k / m)
A = 1


def spring(xv, t):
    return np.asarray(xv[1], cos(xv[0] + t))


def rk4_step(f, xv, t, h):
    k1 = h * f(xv, t)
    k2 = h * f(xv + k1 / 2, t + h / 2)
    k3 = h * f(xv + k2 / 2, t + h / 2)
    k4 = h * f(xv + k3, t + h)
    return xv + k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6


def get_adaptive_step(f, xv, t, h, tol):
    step1 = rk4_step(f, xv, t, h)
    x1 = rk4_step(f, step1, t, h)
    x2 = rk4_step(f, xv, t, 2 * h)
    diff = sqrt(square(x1[0] - x2[0]) + square(x1[1] - x2[1]))
    if diff < tol:
        return 2 * h
    else:
        rho = 30 * h * tol / diff
        if rho < 1:
            return h * pow(rho, 0.25)
        else:
            return h


def ark4_spring(f, x0, v_x0, t_final, h, tol):
    t = 0
    vals = [np.asarray([x0, v_x0])]
    times = [0]
    rk4_step(f, vals[0], t, h)
    while t < t_final:
        h = get_adaptive_step(f, vals[-1], t, h, tol)
        t += h
        times.append(t)
        vals.append(rk4_step(f, vals[-1], t, h))
    return vals, times


points, times = ark4_spring(spring, 1, -1, 10, .1, 1e-3)
plt.plot(times, points)
plt.show()
