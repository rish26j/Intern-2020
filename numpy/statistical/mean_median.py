import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Array:\n", a)

print("\nMedian of array along axis 0:", np.median(a, 0))
print("Mean of array along axis 0:", np.mean(a, 0))
print("Average of array along axis 1:", np.average(a, 1))