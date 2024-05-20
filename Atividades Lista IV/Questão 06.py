import random
r = random.randint(5,20)
n = [random.randint(1,6) for i in range(r)]

d = 1

for i in range (6):
    count = n.count(d)
    print("O Numero %i aparace %i vezes na lista" % (d, count))
    d += 1
