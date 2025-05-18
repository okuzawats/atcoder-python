S = input()
A = [0] * (len(S) + 1)

for i in range(len(S)):
    if S[i] == "<":
        A[i + 1] = max(A[i + 1], A[i] + 1)

for i in range(len(S) - 1, -1, -1):
    if S[i] == ">":
        A[i] = max(A[i], A[i + 1] + 1)

print(sum(A))
