import random

t = int(input("Digite o tamanho da matriz: "))

s = 0

m = [[random.randint(0,9) for i in range(t)] for i in range(t)]

for i in range(t):
    print(m[i])

for i in range(t):
    for j in range(t):
        s += m[i][j]

media = s/(t*t)

print("Soma total é:", s)
print("A média é %.2f" % (media))
