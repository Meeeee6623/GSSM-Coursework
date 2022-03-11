"""
5.7.py
Made by Benjamin Chauhan
"""
import numpy as np
from numpy import arange, sin, sqrt, power, fabs, sum


def f(x):
    return power(sin(sqrt(100 * x)), 2)


def trapezoidal_integral(a, b, n):  # from 5.2
    h = (b - a) / n
    x = arange(1, n)
    return h * (((f(a) / 2) + (f(b) / 2)) + sum(f(a + x * h)))


def adaptive_trapezoidal(a, b, n, desired_error):
    last = trapezoidal_integral(a, b, n)
    err = 9e4
    print(desired_error)
    while err > desired_error:
        print(f'slices: {n}')
        print(f'estimate: {last}')
        print(f'error: {err}')
        n *= 2
        h = (b - a) / n
        k = arange(1, n - 1, 2)
        new = (last / 2) + h * sum(f(a + k * h))
        err = fabs((new - last)) / 3
        last = new
        if n > 10:
            return last
    return last

def recalc_trapezoidal(a, b, n, last):
    h = (b - a) / n
    x = arange(1, n - 1, 2)
    return (last / 2) + h * sum(f(a + x * h))

def romberg_integration(func, a: float, b: float, desired_error: float) -> float:
    """
    Calculates an integral from a to b using romberg integration, stopping when error is below desired_error.
    func: function to integrate over
    a: starting x-value for integration
    b: ending x-value for integration
    desired_error: maximum error desired from integration
    """
    r = np.empty((100, 100))
    r[0, 0] = trapezoidal_integral(a, b, 1)
    r[1, 0] = trapezoidal_integral(a, b, 2)
    i = 1
    n = 2
    err = 9e4
    while err > desired_error:
        for j in range(1, i + 1):
            r[i, j] = (r[i, j] + 1 / (power(4, j + 1) - 1) * (r[i, j] - r[i - 1, j]))

            err = fabs(r[i, j + 1] - r[i - 1, j]) / (power(4, j + 1) - 1)
            if err < desired_error:
                return r[i, j]

        i += 1
        n *= 2
        r[i, 0] = recalc_trapezoidal(a, b, n, r[i - 1, 0])

adaptive_trapezoidal(0, 1, 1, 1e-6)
print(romberg_integration(0, 1, 1e-6))
