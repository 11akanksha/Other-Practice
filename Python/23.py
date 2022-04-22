import sys

def divi(a,b):
    print(int(a/b))
    
def divi_new(func):
    def inner(a,b):
        if a < 0:
            if b < 0:
                a = abs(a)
                b = abs(b)
            elif b > 0:
                b = (-1) * b
                a = abs(a)
        if a<b:
            a,b = b,a
            return func(a,b)
        elif b == 0:
            return func(a,-1)    
        elif a == 0 and b == 0:
            a,b = 1,-1
        return func(a,b)
    return inner
    
divi = divi_new(divi)
a = int(sys.argv[1])
b = int(sys.argv[2])
divi(a,b)
