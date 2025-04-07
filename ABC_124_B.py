n = int(input())
h = [*map(int, input().split())]
c, h_max = 0, 0
for i in range(n):
    if h[i] >= h_max:
        c += 1
    h_max = max(h_max, h[i])
print(c)
