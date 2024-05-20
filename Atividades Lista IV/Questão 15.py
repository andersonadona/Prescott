import random

t1 = int(input("Digite o tamanho da primeira matriz: "))
t2 = int(input("Digite o tamanho da segunda matriz: "))

m1 = [[random.randint(0,9) for i in range(t1)] for i in range(t1)]
m2 = [[random.randint(0,9) for i in range(t2)] for i in range(t2)]
m3 = m1

for i in range(t1):
    print(m1[i])
print()
for i in range(t2):
    print(m2[i])

if t1 == t2:
    for i in range(t2):
        for j in range(t2):
            m3[i][j] += m2[i][j]
    print()
    for i in range(t1):
        print(m3[i])

else:
    print("As matrizes não possuem o mesmo tamanho")