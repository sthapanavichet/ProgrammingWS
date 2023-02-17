import numpy as np

A = np.array([[2, 1], [6, 3]])
B = np.array([3, 3])
print(np.linalg.solve(A, B))

A = np.array([[2, 1], [6, 3]])
B = np.array([1, 3])
print(np.linalg.solve(A, B))

