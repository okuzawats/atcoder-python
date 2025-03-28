n, k = map(int, input().split())
for _ in range(k):
    n = n // 200 if n % 200 < 1 else n * 1000 + 200
print(n)
