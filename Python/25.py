import sys

a, b = int(sys.argv[1]), int(sys.argv[2])

if a*b < 1000:
    print(a*b)
else:
    print(a+b)

#----------------

import sys

a = int(sys.argv[1])

if a%2 == 0:
    print('Even')
else:
    print('Odd')

#-------------

import sys

n = int(sys.argv[1])
i = 2
while i < (n+2):
    s = sys.argv[i]
    j = len(s)
    ans = ''
    for k in range(j):
        if k % 2 == 0:
            ans = ans + (s[k] + ' ')
    print(ans[:-1])
    i = i + 1

#-----------------

import sys

num1, num2, num3 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
l = [num1, num2, num3]
print(max(l),min(l),int(sum(l)/len(l)))

#-------------

import sys

n = int(sys.argv[1])
s = set()
for i in range(n):
    s.add(int(sys.argv[i+2]))

s.remove(max(s))
print(max(s))
