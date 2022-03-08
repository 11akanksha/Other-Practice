def show(n = 2):
    print(n**2)
# then we can make a process' list:
procs = []

# then we can create a new process by saying:
# pr = Process(target = show)
# target is the function that'll be ran in this particular process.

To create 5 processes:
for i in range(5):
    procs.append(Process(target = show))
    
# to start all these processes:
for proc in procs:
    proc.start()

# to see their results:
for p in procs:
    p.join()
    
# Here we see that the o/p of below is as shown:

# to start all these processes:
for proc in procs:
    proc.start()
 
 #O/p:
 4
 4
 4
 4
 4
