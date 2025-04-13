N, S, A = int(input()), input(), ""
for s in S:
    c = ord(s) + N
    if c > 90:
        c -= 26
    A += chr(c)
print(A)
