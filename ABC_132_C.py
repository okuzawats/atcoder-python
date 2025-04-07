N, D = int(input()), [*map(int, input().split())]
D.sort()
print(D[N // 2] - D[N // 2 - 1])
