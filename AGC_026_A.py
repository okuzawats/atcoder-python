N = int(input())
A = [*map(int, input().split())]

ans = 0
for i in range(1, N):
    if A[i - 1] == A[i]:
        ans, A[i] = ans + 1, None

print(ans)
