S, A = input(), []

i = 1
while i < len(S):
    j = i
    while S[j].islower():
        j += 1
    A.append(S[i - 1 : j + 1])
    i = j + 2
print("".join(sorted(A, key=lambda s: s.lower())))
