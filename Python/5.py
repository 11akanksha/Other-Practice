# implementing cout of C++ in python:
class Ostream:
    def __lshift__(self,other):
        print(other, end = '')
        return self

cout = Ostream()
cout<<"hello"<<"world"

#O/p:
helloworld
