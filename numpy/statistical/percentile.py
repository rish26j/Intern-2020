import numpy as np

a = np.array([[2, 10, 20], [80, 43, 31], [22, 43, 10]])

print("Array:\n", a)

print("\nPercentile along axis 0", np.percentile(a, 10, 0))

print("Percentile along axis 1", np.percentile(a, 10, 1))