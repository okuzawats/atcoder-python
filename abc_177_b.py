S = input()
T = input()
m = len(T)
for i in range(len(S)-len(T)):
    l = len(T)
    for j in range(l):
        if S[i+j] == T[j]:
            l -= 1
    m = min(m, l)
print(m)
