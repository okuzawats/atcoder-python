a, b, c, x = int(input()), int(input()), int(input()), int(input())

ans = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            ans += 1 if 500 * i + 100 * j + 50 * k == x else 0
print(ans)
