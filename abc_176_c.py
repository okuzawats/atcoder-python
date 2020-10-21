N = int(input())
A = list(map(int, input().split()))
s = 0
for i in range(N - 1):
    if A[i] <= A[i + 1]:
        continue
    h = A[i] - A[i + 1]
    A[i + 1] += h
    s += h
print(s)
