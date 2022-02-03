import numpy as np
from numpy import array, empty

A = array([[2, 1, 4, 1],
           [3, 4, -1, -1],
           [1, -4, 1, 5],
           [2, -2, 1, 3]], float)
v = array([-4, 3, 9, 7], float)
N = len(v)

for m in range(N):
    max_ind = np.argmax(A[:, m])  # get index of max row for current column
    if max_ind > m:
      A[[m, max_ind], :] = A[[max_ind, m], :]  # swap rows (pivot)
      v[m], v[max_ind] = v[max_ind], v[m]  # swap vector
      print(f'swapped {m}, {max_ind}')

    print(A)

    A[m, m:] /= A[m, m]
    v[m] /= A[m, m]
    print(A)

    if m + 1 < N:
        A[m+1:, m:] -= A[m + 1:, m, np.newaxis] * np.concatenate(([[A[m, m:]]] * (N - m - 1)))  # subtract scaled value from lower rows
    print(A)
    print()

    # back substitute
x = empty(N)
for m in range(N-1, -1, -1):
  x[m] = v[m] - sum(A[m, m+1:N] * x[m+1:N])

print(x)

'''x = empty(N,float)
for m in range(N-1,-1,-1):
x[m] = v[m]
for i in range(m+1,N):
x [m] -= A [m, i] *X [i]
print(x)'''
