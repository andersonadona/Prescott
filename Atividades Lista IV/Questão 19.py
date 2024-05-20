import random

r = random.randint(5,25)
l = [random.randint(0,9) for i in range (r)]
impar = []
par = []

d = 0

print(l)

for i in range(r):
    d = l[i] % 2
    if d == 1:
        impar.append(l[i])
    else:
        par.append(l[i])

print()
print(impar)
print(par)
print()
print(par+impar)