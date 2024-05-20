import random

l = []
n = 20

while len(l) != n:
    r = random.randint(0,n-1)
    if r not in l:
        l.append(r)

l1 = sorted(l)
l2 = []
n1 = len(l) - 1

t = int((len(l))/2)

for i in range (t):
    l2.append(l1[i])
    l2.append(l1[n1])
    n1 -= 1

print (l)
print (l2)