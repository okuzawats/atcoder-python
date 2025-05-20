N = int(input())
A = [*map(int, input().split())]

ans, i = 0, 0
while i < N:
    while i + 1 < N and A[i] == A[i + 1]:
        i += 1
    if i + 1 < N and A[i] < A[i + 1]:
        while i + 1 < N and A[i] <= A[i + 1]:
            i += 1
    elif i + 1 < N and A[i] > A[i + 1]:
        while i + 1 < N and A[i] >= A[i + 1]:
            i += 1
    ans, i = ans + 1, i + 1
print(ans)
