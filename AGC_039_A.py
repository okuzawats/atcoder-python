S, K = input(), int(input())

c, i = 0, 1
while i < len(S):
    if S[i - 1] == S[i]:
        c += 1
        i += 1
    i += 1

S2 = S * 2
c2, i = 0, 1
while i < len(S2):
    if S2[i - 1] == S2[i]:
        c2 += 1
        i += 1
    i += 1

print((K - 2) * c + c2)
