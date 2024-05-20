import random

t = 5
m = [[random.randint(0,9) for i in range(t)] for i in range(t)]
d = 0
s = 0

for i in range(t):
    print(m[i])

for i in range(t):
    s += m[i][d]
    d += 1

print ("Soma da diagonal principal é:",s)

s = 0
d = t - 1

for i in range(t):
    s += m[i][d]
    d -= 1

print ("Soma da diagonal secundaria é:",s)