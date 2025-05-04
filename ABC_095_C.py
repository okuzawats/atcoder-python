A, B, C, X, Y = map(int, input().split())

ans = 5000 * 10**5
for c in range(0, max(X, Y) * 2 + 1):
    a = max(0, X - c // 2)
    b = max(0, Y - c // 2)
    ans = min(ans, a * A + b * B + c * C)
print(ans)
