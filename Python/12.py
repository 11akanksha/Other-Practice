# generator expressions

gen = (x**2 for x in range(1,11))
print(gen)
print(type(gen))
print()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#O/p:
<generator object <genexpr> at 0x7f9caa9f5580>
<class 'generator'>

1
4
9
16
25
36
49
64
81
100
Traceback (most recent call last):
  File "<string>", line 15, in <module>
StopIteration
