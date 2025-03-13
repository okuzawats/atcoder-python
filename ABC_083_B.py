n, a, b = [*map(int, input().split())]

ans = 0
for i in range(1, n + 1):
    s = sum(map(int, [*str(i)]))
    if a <= s and s <= b:
        ans += i
print(ans)
