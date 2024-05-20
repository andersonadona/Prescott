import random

r = random.randint(5,25)
l = [random.randint(0,9) for i in range (r)]
a = []

for i in range(r):
    if not l[i] in a:
        a.append(l[i])

print(l)
print(a)