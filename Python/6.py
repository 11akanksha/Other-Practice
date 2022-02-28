class Cat:
    breed = 'Siberian'
    
    def __init__(self,name):
        self.name = name

c1 = Cat('Amy')
print(c1.breed)

c2 = Cat('Fluffy')
c2.breed= 'Exotic shorthair'
print(c2.breed)
print(c1.breed)

#O/p:
Siberian
Exotic shorthair
Siberian
