n, x = map(int, input().split())
l = list(map(int, input().split()))
a, c = 1, 0

for i in range(n):
    c += l[i]
    if c <= x:
        a += 1
    else:
        print(a)
        exit()
print(a)
