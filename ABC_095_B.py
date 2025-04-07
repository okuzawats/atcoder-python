n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
print((x - sum(m)) // min(m) + n)
