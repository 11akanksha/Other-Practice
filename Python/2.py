users = {
    "abc" : "123",
    "def" : "456",
    "ghi" : "789"
}

def checker(functn):
    def check(username,password,*args,**kwargs):
        if username in users and users[username] == password:
            functn(*args)
        else:
            print("Error")
    return check

@checker
def message(name):
    print("Hello {} , today is your lucky day!".format(name))

message("def","456","Justin")
message("def","4567","Justin")

#O/p:
Hello Justin , today is your lucky day!
Error

--------------------------------------------------------

li = ["a","b","c"]

def symbol_checker(fun):
    def check(symbol,**kwargs):
        if symbol in li:
            fun(**kwargs)
        else:
            print("symbol mismatch")
    return check
    
@ symbol_checker
def show(**d):
    print(d)

show("a",key1 = "val1",key2="val2")

#O/p:
{'key1': 'val1', 'key2': 'val2'}
------------------------------------------

li = ["a","b","c"]

def symbol_checker(fun):
    def check(symbol,**kwargs):
        if symbol in li:
            fun(**kwargs)
        else:
            print("symbol mismatch")
    return check
    
@ symbol_checker
def show(**d):
    print(d)
    for i in d:
        print(i,d[i])

show("a",key1 = "val1",key2="val2")

#O/p:
{'key1': 'val1', 'key2': 'val2'}
key1 val1
key2 val2
