import random

r = random.randint(1,15)
n = [random.randint(0,9) for i in range(r)]

print(n)

u = int(input("Digite qual valor queira remover da lista: "))

for i in range(r):
    if n[i] == u:
        n[i] = "*"

print(n)