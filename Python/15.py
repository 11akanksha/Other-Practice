import numpy as np

# a tensor:
# has 6 rows, 5 columns and 3 channels
d = np.ones((6,5,3))
print(d)
print(d.shape)

#O/p:
[[[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]]
(6, 5, 3)

#-----------------------------------

import numpy as np

a = np.array([[1],[2],[3]])
print(a)
print(a.shape)
print(a[1][0],'\n')
b = a.T
print(b)
print(b.shape)
print(b[0][1])

#O/p:
[[1]
 [2]
 [3]]
(3, 1)
2 

[[1 2 3]]
(1, 3)
2

#----------------------------------------

import numpy as np

b = np.zeros((50,25,3),dtype = 'uint8')
b[:,:,2] = 200
print(b.shape)
c = np.transpose(b)
print(c.shape)
d = np.transpose(b,axes = (0,2,1))
print(d.shape)

#O/p:
(50, 25, 3)
(3, 25, 50)
(50, 3, 25)
