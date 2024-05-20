n = []
p = []
t = 0
m = 0

r = int(input("Digite quantas notas deseja lancar: "))

for i in range (r):
    n.append(int(input("Digite a sua nota: ")))
    p.append(int(input("Digite o peso da nota: ")))

for i in range (r):
    t = t + p[i]
if t > 10:
    print("O peso das notas informados é superior a 10, revise o peso.")
elif t < 10:
    print("O peso das notas informados é superior a 10, revise o peso.")
elif t == 10:
    for i in range (r):
        m = m + (n[i]*p[i])
    m = m / 10

print("Sua média é:",m)