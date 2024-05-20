import random
n = []

r = int(input("Digite quantas palavras deseja informar: "))

for j in range (r):
    n.append(str.casefold(input("Ditige a palavra: ")))

v = ["a", "e", "i", "o", "u"]
o = [0, 0, 0, 0, 0]

for i in range (r):
    for j in range (len(n[i])):
            for z in range (5):
                if v[z] == n[i][j]:
                    o[z] += 1

print()

for i in range (len(v)):
     print("A letra",v[i],"repete",o[i],"vezes")