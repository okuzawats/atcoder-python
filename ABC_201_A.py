A = sorted([*map(int, input().split())])
print("Yes" if A[2] - A[1] == A[1] - A[0] else "No")
