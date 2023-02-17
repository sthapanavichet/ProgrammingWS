import numpy as np

A =  np.array([[2, 1, 3], [1, -1, 2], [4, 3, 5]])
B = np.array([-9, -7, -15])

print(np.linalg.det(A))
print(np.linalg.solve(A,B))


