class A:
    def __init__(self,n):
        self.n = n
    
    def __str__(self):
        return str(self.n)
    
    def __enter__(self):
        return self
    
    def __exit__(self,*args):
        print(args)
        return True
        
with A(5) as a:
    print(a)
    raise 10/0
print('Hello')

#O/p:
5
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x7f0a5fe82940>)
Hello
