# Média dos Elementos: Desenvolva um algoritmo que calcule e retorne a média dos elementos de uma lista de números.
import random

r = random.randint(1,15)
n = [random.randint(0,9) for i in range(r)]
s = 0

for i in range(r):
    s += n[i]

m = s / r

print("A média é", m)
print(n)
