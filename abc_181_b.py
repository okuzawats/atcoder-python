P = [map(int, input().split()) for _ in range(int(input()))]
s = 0
for a, b in P:
    s += (a + b) * (b - a + 1) // 2
print(s)
