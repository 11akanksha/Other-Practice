from functools import reduce

a = [1,2,3,4,5,8,9,10,215]
# find sum of all values:
s = reduce(lambda i,j : i+j,a)
print(s)

#o/p:
257
