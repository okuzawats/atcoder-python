N, K = map(int, input().split())
H = sorted([int(input()) for _ in range(N)])

ans = 10**9
for i in range(N - K + 1):
    mx = H[i + K - 1]
    mn = H[i]
    ans = min(ans, mx - mn)

print(ans)
