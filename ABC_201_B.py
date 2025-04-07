n, m = int(input()), []
for _ in range(n):
    M, T = map(str, input().split())
    m.append([int(T), M])
print(sorted(m)[len(m) - 2][1])
