import numpy as np
from numpy import linalg as LA


def my_fun(m):
    return LA.norm(m, ord=np.inf, axis=None)  # inf - для матриць поертається np.max(np.sum(np.abs(x), axis=1))


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
norms = my_fun(a)
print(norms)
