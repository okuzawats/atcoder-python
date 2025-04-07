n, d = map(int, input().split())
a = 0
for i in range(n):
    x, y = map(int, input().split())
    if x**2 + y**2 <= d**2:
        a += 1
print(a)
