N, S = int(input()), input()
c, p = 0, ""
for s in S:
    if s != p:
        c, p = c + 1, s
print(c)
