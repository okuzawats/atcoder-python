N, M = map(int, input().split())
S = [[*map(int, input().split())] for _ in range(M)]

for i in range(10**N):
    if len(str(i)) == N and all(str(i)[s - 1] == str(c) for s, c in S):
        print(i)
        exit()
print(-1)
