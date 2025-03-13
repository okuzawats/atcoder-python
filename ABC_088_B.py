n = int(input())
a = [*map(int, input().split())]
a.sort(reverse=True)
s = 0
for i in range(n):
    if i % 2 < 1:
        s += a[i]
    else:
        s -= a[i]
print(s)
