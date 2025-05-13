N, D = map(int, input().split())
X = [[*map(int, input().split())] for _ in range(N)]

c = 0
for i in range(N):
    for j in range(i + 1, N):
        d2 = 0
        for k in range(D):
            d2 += (X[i][k] - X[j][k]) ** 2
        d = d2**0.5
        if d == int(d):
            c += 1
print(c)
