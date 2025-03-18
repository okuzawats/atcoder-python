n, y = map(int, input().split())

for i in range(n + 1):
    for j in range(n + 1):
        k = n - i - j
        if k < 0:
            continue
        if i * 10000 + j * 5000 + k * 1000 == y:
            print(i, j, k)
            exit()

print(-1, -1, -1)
