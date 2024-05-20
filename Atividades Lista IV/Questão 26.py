import random

t = 5
m = [[random.randint(0,1) for i in range(t)] for i in range(t)]
s = 0

for i in range(t):
    print(m[i])
print()

for i in range(t):
    for j in range(t):
        if m[i][j] == 0:
            s += 1

if s > (t * t / 2):
    print("A matriz é esparsa, pois contem",s,"vezes o 0.")
else:
    print("A matriz não é esparsa, pois contem apenas",s,"vezes o 0.")