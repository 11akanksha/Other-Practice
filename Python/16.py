import numpy as np

a = np.array([
    [2,3],
    [3,1]
    ])
b = np.array([8,5])
print(np.linalg.solve(a,b))

#O/p:
[1. 2.]
