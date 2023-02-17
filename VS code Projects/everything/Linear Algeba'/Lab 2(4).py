import numpy as np

np.random.seed(1)

A = 10 * np.random.rand(10, 10) - 5
B = 10 * np.random.rand(10) - 5

solution = np.linalg.solve(A, B)
print(solution)

print(sum(abs(np.dot(A, solution) - B)))


