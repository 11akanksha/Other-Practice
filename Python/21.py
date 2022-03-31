import sys


class Flight:
    def __init__(self, tno, d_city, arr_city, fno, sno):
        self.tno = tno
        self.d_city = d_city
        self.arr_city = arr_city
        self.fno = fno
        self.sno = sno

    def display(self):
        print('Ticket Number: ', self.tno)
        print('Departure: ', self.d_city)
        print("Arrival: ", self.arr_city)
        print("Flight number: ", self.fno)
        print("Seat number: ", self.sno)


j = 2
f = []
for _ in range(int(sys.argv[1])):
    f.append(Flight(sys.argv[j], sys.argv[j+1], sys.argv[j+2],
                    sys.argv[j+3], sys.argv[j+4]))
    j = j + 5

for i in range(int(sys.argv[1])):
    f[i].display()
