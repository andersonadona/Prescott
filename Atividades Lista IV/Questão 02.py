a = int(input("Digite lado 1: "))
l = int(input("Digite lado 2: "))

r = 0
n = l - 4

if a <= 2:
    for i in range(a):
        print("*" * l)
else:
    for i in range(a):
        r = r + 1
        if r == a or r == 1:
            print("*" * l)
        else:
            print("*"," "*n,"*")
