S = input()
T = input()
t = len(T)
a = t
for i in range(len(S) - t + 1):
    l = len(T)
    for j in range(l):
        if S[i+j] == T[j]:
            l -= 1
    a = min(a, l)
print(a)
