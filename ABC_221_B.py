S, T = input(), input()

if S == T:
    print("Yes")
    exit()

L = len(S)
for i in range(1, L):
    s = list(S)
    s[i - 1], s[i] = s[i], s[i - 1]
    if "".join(s) == T:
        print("Yes")
        exit()
print("No")
