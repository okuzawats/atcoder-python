c = 0
for _ in range(int(input())):
    l, r = map(int, input().split())
    c += r - l + 1
print(c)
