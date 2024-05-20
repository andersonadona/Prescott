import random

r = random.randint(5,25)

t = tuple(random.randint(0,9) for i in range (r))

print(t)
print(t[::-1])