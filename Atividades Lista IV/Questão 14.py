import random

r = 10
n1 = [random.randint(0,100) for i in range(r)]
n2 = [random.randint(0,100) for i in range(r)]

a = []

for i in range(r):
    if not n1[i] in n2:
        a.append(n1[i])

print(n1)
print()
print(n2)
print()
print(a)