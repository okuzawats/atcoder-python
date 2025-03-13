n = int(input())
a = [*map(int, input().split())]
a.sort(reverse=True)
s = 0
for i in range(n):
    s += a[i] if i % 2 < 1 else -a[i]
print(s)
