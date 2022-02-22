def div(a,b):
    try:
        return a/b
    except:
        print('Error')
    finally:
        print("You attempted to divide.")
        
quotient = div(2,3)
print("{} divided by {} gives {}".format(2,3,quotient))
div(2,0)

#O/p:
You attempted to divide.
2 divided by 3 gives 0.6666666666666666
Error
You attempted to divide.



def div(a,b):
    try:
        return a/b
    except:
        print('Error')
    finally:
        print("You attempted to divide.")
        return "haha"
        
quotient = div(2,3)
print("{} divided by {} gives {}".format(2,3,quotient))
quotient = div(2,0)
print("{} divided by {} gives {}".format(2,0,quotient))


#O/p:
You attempted to divide.
2 divided by 3 gives haha
Error
You attempted to divide.
2 divided by 0 gives haha
