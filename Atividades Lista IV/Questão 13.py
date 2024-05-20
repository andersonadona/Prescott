import random

r = random.randint(5,25)
n = [random.randint(0,9) for i in range(r)]

print("Digite 1, para odernar em ordem crescente")
print("Digite 2, para odernar em ordem decrescente")
a = int(input("Escolha como deseja ordernar a lista: "))

if a == 1:
    print(sorted(n))

if a == 2:
    print(sorted(n,reverse=True))