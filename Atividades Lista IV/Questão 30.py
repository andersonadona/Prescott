import random

t = 10
m1 = [random.randint(0,15) for i in range(t)]
m2 = [random.randint(0,15) for i in range(t)]
m3 = m1 + m2
m4 = []
r = 0

for i in range (len(m3)):
    for j in range (len(m3)):
        if m3[i] == m3[j]:
            r += 1
    if r == 1:
        m4.append(m3[i])
    r = 0

print(sorted(m1))
print(sorted(m2))
print()
print(sorted(m4))
