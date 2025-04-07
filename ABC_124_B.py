n = int(input())
h = [*map(int, input().split())]
c, m = 0, 0
for i in h:
    if i >= m:
        c += 1
    m = max(m, i)
print(c)
