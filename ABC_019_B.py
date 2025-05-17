S = input()
r, i = [], 0
while i < len(S):
    j = i
    while j < len(S) and S[j] == S[i]:
        j += 1
    r.append([S[i], j - i])
    i = j
print("".join(map(lambda p: f"{p[0]}{p[1]}", r)))
