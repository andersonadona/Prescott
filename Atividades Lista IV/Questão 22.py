import random

r = random.randint(5,25)
l1 = tuple(random.randint(0,9) for i in range (r))
l2 = tuple()

for i in range (r):
    count = l1.count(l1[i])
    if count == 1:
        l2 += (l1[i],)

print(l1)
print(l2)