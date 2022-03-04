class myException(Exception):
    def __init__(self,message):
        self.message = message
    
    def __str__(self):
        return self.message

try:
    raise myException('some error')
except Exception as e:
    print(e)

#O/p:
some error
