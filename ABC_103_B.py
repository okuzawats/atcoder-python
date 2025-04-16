S, T = input(), input()
L = len(S)
for i in range(L):
    if S[i : i + L] + S[0:i] == T:
        print("Yes")
        exit()
print("No")
