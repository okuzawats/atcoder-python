N, M = map(int, input().split())
S = [[*map(int, input().split())] for _ in range(M)]

for i in range(10**N):
    n = str(i)
    if len(n) != N:
        continue
    for s, c in S:
        if n[s - 1] != str(c):
            break
    else:
        print(n)
        exit()
print(-1)
