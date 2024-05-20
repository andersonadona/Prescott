# Escreva um algoritmo que encontre e retorne o maior elemento em uma lista de números.
import random

r = random.randint(1,15)
n = [random.randint(0,9) for i in range(r)]

print(max(int(n) for n in n))
print(min(int(n) for n in n))
