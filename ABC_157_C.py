N, M = map(int, input().split())
S = [[*map(int, input().split())] for _ in range(M)]

for i in range(10**N):
    n = str(i)
    if len(n) == N and all(n[s - 1] == str(c) for s, c in S):
        print(n)
        exit()
print(-1)
