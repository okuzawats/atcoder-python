k, s = map(int, input().split())

c = 0
for x in range(k + 1):
    for y in range(k + 1):
        for z in range(k + 1):
            if x + y + z == s:
                c += 1

print(c)
