import numpy as np

a = np.array(99)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)