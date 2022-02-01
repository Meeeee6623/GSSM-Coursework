import math
import time

# pi integral evaluator, given N
import numpy
from numpy import linspace, sqrt, arange, power, float64


def evaluate_pi(N):
    h = 2 / N
    x = linspace(-1, 1, N)
    y = sqrt(1 - x ** 2)
    return h * sum(y)


def check_estimate(estimate):
    print(f'Your estimate was: {estimate}')
    print(f'Real value of pi: {math.pi}')
    print(f'Error: {math.fabs(math.pi - estimate)}')


'''a) Write a program to evaluate the integral above with N == 100 and compare the
result with the exact value. The two will not agree very well, because N == 100 is
not a sufficiently large number of slices. '''

N = 100
estimate = evaluate_pi(N)
check_estimate(estimate)

'''b) Increase the value of N to get a more accurate value for the integral. If we require
that the program runs in about one second or less, how accurate a value can you
get? '''

# times = []
# for i in range(1000000, 1000000000000, 500000):
#     now = time.time()
#     evaluate_half_pi(i)
#     elapsed = time.time() - now
#     if elapsed > 1:
#         times.append(i)
#         break
#     if len(times) == 0:  # first time
#         times.append(elapsed)
#     else:
#         times.append(elapsed)
#         times.pop(0)
#     print(elapsed)
# print(times)
# check_estimate(evaluate_half_pi(times[1]))

'''also compute pi using the Leibniz formula and the Bailey–Borwein–Plouffe formula.'''


def leibniz_pi(N):
    k = arange(0, N + 1)
    y = (-1) ** k / (2 * k + 1)
    return sum(y) * 4


def bbp_pi(N):
    k = arange(N + 1)
    y = 1 / power(float64(16), k) * \
        (4 / (8 * k + 1) -
         2 / (8 * k + 4) -
         1 / (8 * k + 5) -
         1 / (8 * k + 6))
    print(y)
    return sum(y)
    pass


N = 10
leibniz = leibniz_pi(N)
print(leibniz)
print(check_estimate(leibniz))
bbp = bbp_pi(N)
print(bbp)
print(check_estimate(bbp))
