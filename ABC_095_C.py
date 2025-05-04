A, B, C, X, Y = map(int, input().split())
ans = 10**18
for c in range(max(X, Y) * 2 + 1):
    ans = min(ans, max(0, X - c // 2) * A + max(0, Y - c // 2) * B + c * C)
print(ans)
