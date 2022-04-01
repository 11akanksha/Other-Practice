import sys


class BCust:
    def __init__(self, name):
        self.name = name


class BAcc(BCust):
    def __init__(self, fName, lName, num_acc, bal):
        name = fName + " " + lName
        super().__init__(name)
        self.num_acc = num_acc
        self.balance = bal

    def display(self):
        print('Name: ', self.name)
        for i in range(self.num_acc):
            print('Account ', i+1, ' balance: ', self.balance[i])


acc = int(sys.argv[3])
b = []
j = 4
for i in range(acc):
    b.append(sys.argv[j])
    j = j+1


customer = BAcc(sys.argv[1], sys.argv[2], acc, b)
customer.display()
