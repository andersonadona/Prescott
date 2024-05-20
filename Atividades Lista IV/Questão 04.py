m = [[0,0,0,0,0]] * 5
e = 0
d = 4

for i in range(5):
    for j in range(5):
        if j == e and j == d:
            m[i][j] = 3
        elif j == e or j == d:
            m[i][j] = 1
        else:
            m[i][j] = 0
    d -= 1
    e += 1
    print(m[i])
