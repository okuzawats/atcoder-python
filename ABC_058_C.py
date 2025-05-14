N, c_m = int(input()), [10**5] * 26
for _ in range(N):
    S, c_s = input(), [0] * 26
    for c in S:
        c_s[ord(c) - 97] += 1
    for i in range(26):
        c_m[i] = min(c_m[i], c_s[i])
print("".join([chr(i + 97) * c_m[i] for i in range(26)]))
