# swap values of 2 variables:

# 1st method:
a = 2
b = 5
print(a,b)
temp = a
a = b
b = temp
print(a,b)

# 2nd method:
#(will work only with integers)
a = 4
b = 10
print(a,b)
a = a+b
b = a-b
a = a-b
print(a,b)

# 3rd method:
a = 9
b = 3
print(a,b)
a = a^b
b = a^b
a = a^b
print(a,b)

# 4th method:
#(unique to python)
a = 10
b = 12
print(a,b)

(a,b) = (b,a)
print(a,b)

# OR:
a = 20
b = 21
print(a,b)
a,b = b,a
print(a,b)

#O/p:
2 5
5 2
4 10
10 4
9 3
3 9
10 12
12 10
20 21
21 20
