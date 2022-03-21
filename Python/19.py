m = [1,2,3,4,5]

# non pythonic:
if len(m) >= 6:
    print(m[5])
else:
    print("That index doesn't exist")
# in the above we asked permission- we asked if the len is >=6 or not.
    
# pythonic:
try:
     print(m[5])
except IndexError:
    print("That index doesn't exist")
    
#O/P:
That index doesn't exist
That index doesn't exist
