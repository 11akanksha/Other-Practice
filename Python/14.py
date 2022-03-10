import numpy as np

b = np.array([1,5,8,4,6])
w = np.array([1,2,3,4,5])
print(np.mean(b))
print(np.average(b,weights = w))

#O/p:
4.8
5.4

#-------------------------------------

import numpy as np

c = np.array([1,2,9,8,4])
u = np.mean(c)
σ = np.sqrt(np.mean(abs(c-u)**2))
print(σ)

#O/p:
3.1874754901018454

#-----------------------------------

import numpy as np

c = np.array([1,2,9,8,4])
print(np.std(c))

#O/p:
3.1874754901018454

#----------------------------------

import numpy as np

c = np.array([1,2,9,8,4])
u = np.mean(c)
σ = np.sqrt(np.mean(abs(c-u)**2))
print(σ**2)

# Using inbuilt function:
print(np.var(c))

#O/p:
10.16
10.16
