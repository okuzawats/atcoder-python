S = input()
c, m = 0, 0
for s in S:
    if s == 'R':
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)
