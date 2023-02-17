from ftplib import B_CRLF
import numpy as np

A = np.array([[2, 3], [1, -2], [0, 1]])
B = np.array([[5, 0, -3], [-2, -2, -3]])
B_transposed = np.transpose(B) 

print(np.dot(A, B))
print(np.subtract(A, B_transposed))