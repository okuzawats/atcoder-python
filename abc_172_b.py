S, T = input(), input()
c = 0
for s, t in zip(S, T):
    c += s != t
print(c)
