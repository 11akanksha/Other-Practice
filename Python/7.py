with open('hello.txt','r') as file :
  print(file.read())
  file.seek(5)
  print(file.read())
print(file.read())

#O/p:
Hello
Hello again
Hello yet again

Hello again
Hello yet again

ValueError: I/O operation on closed file.
