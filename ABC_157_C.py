N, M = map(int, input().split())
S = [[*map(int, input().split())] for _ in range(M)]

for i in range(10 ** (N - 1), 10**N):
    num = str(i)
    if len(num) == N:
        for s, c in S:
            if num[s - 1] != str(c):
                break
        else:
            print(num)
            exit()
print(-1)
