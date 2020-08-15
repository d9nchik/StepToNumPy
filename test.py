import numpy as np

list_a = [1, 2, 3, 4]
array_a = np.array(list_a)

list_b = [11, 22, 33, 44]
array_b = np.array(list_b)

print(array_a + array_b)  # [12 24 36 48]

print(array_a * 3)  # [3 6 9 12]

print(array_a.shape)
