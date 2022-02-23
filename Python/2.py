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
