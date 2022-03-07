class myRange:
    def __init__(self,n):
        self.i = 0
        self.n = n
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

for x in myRange(5):
    print(x)

print()
y = myRange(5)
y_iter = iter(y)
print(y_iter)
print()
print(next(y_iter))
print(next(y_iter))
print(next(y_iter))
print(next(y_iter))
print(next(y_iter))
print(next(y_iter))

#O/p:
0
1
2
3
4

<__main__.myRange object at 0x7fe62945ed90>

0
1
2
3
4
Traceback (most recent call last):
  File "<string>", line 30, in <module>
  File "<string>", line 15, in __next__
StopIteration
