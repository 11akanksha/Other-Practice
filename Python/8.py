try:
    a = 10/0
except Exception as e:
    print(e)

#O/p:
division by zero

#-------------------------------------------------

try:
    print(15/0)
    a = int('apple')
except ZeroDivisionError:
    print('you are tyring to convert string to int')
except ValueError:
    print('hahaha')
   
#O/P:
you are tyring to convert string to int
