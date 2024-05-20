import random

t = 5
m = [[random.randint(0,9) for i in range(t)] for i in range(t)]

for i in range(t):
    print(m[i])

print()

u = int(input("Digite qual valor deseja colocar na matriz: "))

print()

for i in range(t):
    for j in range(t):
        m[i][j] = u

for i in range(t):
    print(m[i])