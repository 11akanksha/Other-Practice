# remove duplicates from list:
l = [1,2,3,4,1,2,3,4]
# solution:
l = list(set(l))
print(l)

#O/p:
[1, 2, 3, 4]

#-------------------------------
# list of all even numbers' squares from 0 to 9:
print([i**2 for i in range(10) if i%2 == 0])

#O/p:
[0, 4, 16, 36, 64]

print({i:i**2 for i in range(10) if i % 2 == 0})

#O/p:
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

#---------------------------------------------------------

print({i**2 for i in range(10) if i % 2 == 0})

#O/p:
{0, 64, 4, 36, 16}

#---------------------------------------------

print(type(i**2 for i in range(10)))

#O/p:
<class 'generator'>
#---------------------------------------------
