import sys
import time
import math

def factorial(val):
    time.sleep(1)
    return math.factorial(val)

def time_taken(func):
    start_time = time.time()
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
    return inner
    
factorial = time_taken(factorial)
no = int(sys.argv[1])
print(factorial(no))

