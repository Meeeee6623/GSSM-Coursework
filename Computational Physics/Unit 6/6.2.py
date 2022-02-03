import numpy as np
from numpy import array

A = array([[2, 1, 4, 1],
           [3, 4, -1, -1],
           [1, -4, 1, 5],
           [2, -2, 1, 3]], float)
v = array([-4, 3, 9, 7], float)
N = len(v)

for m in range(N):
    max_ind = np.argmax(A[m:, m], axis=0)  # get max row below current
    A[[m, max_ind], :] = A[[max_ind, m], :]  # swap rows (pivot)
    v[m], v[max_ind] = v[max_ind], v[m]  # swap vector

    A[m, :] /= A[m, m]
    v[m] /= A[m, m]

    if m + 1 < N:
        A[m+1:, :] -= A[m + 1:, m, np.newaxis] * np.concatenate(([[A[m, :]]] * 3))  # subtract scaled value from lower rows
    print(A)
    exit()
