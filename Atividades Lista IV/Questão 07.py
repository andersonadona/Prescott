n = int(input("Quantos numeros ira ter na lista? "))
lista = []
s = 0

for i in range(n):
    lista.append(int(input("Digite o numero: ")))
    s += lista[i]

print("A soma é:", s)
