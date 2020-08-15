import numpy as np

a = int(input())
if input() == '0':
    print(np.zeros((a, a)))
else:
    print(np.ones((a, a)))
