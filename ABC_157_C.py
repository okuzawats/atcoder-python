N, M = map(int, input().split())
S = [[*map(int, input().split())] for _ in range(M)]

for i in range(10**N):
    n = str(i)
    if len(n) != N:
        continue
    if any(n[s - 1] != str(c) for s, c in S):
        continue
    print(n)
    exit()
print(-1)
