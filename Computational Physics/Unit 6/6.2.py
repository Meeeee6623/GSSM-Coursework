import numpy as np
from numpy import array, sum


def solve_gaussian(A: np.ndarray, v: np.ndarray):
    N = len(v)
    if len(v) != A.shape[0] or A.shape[0] != A.shape[1]:
        return Exception(
            '''Array sizes incompatible. Make sure A is a square array, and the length of v matches that of A.''')

    for m in range(N):
        max_ind = np.argmax(A[:, m])  # get index of max row for current column
        if max_ind > m:
            A[[m, max_ind], :] = A[[max_ind, m], :]  # swap rows (pivot)
            v[m], v[max_ind] = v[max_ind], v[m]  # swap vector

        v[m] /= A[m, m]
        A[m, m:] /= A[m, m]

        if m + 1 < N:
            v[m + 1:] -= v[m] * A[m + 1:, m]  # subtract scaled vector value from lower rows
            A[m + 1:, m:] -= np.einsum('i,ij->ij', A[m + 1:, m], np.concatenate(
                ([[A[m, m:]]] * (N - m - 1))))  # subtract scaled matrix value from lower rows

    # back substitute
    x = array([0] * N, float)
    for m in range(N - 1, -1, -1):
        x[m] = v[m] - sum(A[m, m + 1:] * x[m + 1:])
    return x


# Eq. 6.1
arr = array([[2, 1, 4, 1],
             [3, 4, -1, -1],
             [1, -4, 1, 5],
             [2, -2, 1, 3]], float)
v = array([-4, 3, 9, 7], float)

print(solve_gaussian(arr, v))
print(np.linalg.solve(arr, v))

# Eq. 6.17
arr = array([[0, 1, 4, 1],
             [3, 4, -1, -1],
             [1, -4, 1, 5],
             [2, -2, 1, 3]], float)
v = array([-4, 3, 9, 7], float)
print(solve_gaussian(arr, v))
print(np.linalg.solve(arr, v))
