N, A = int(input()), [*map(int, input().split())]
print("Yes" if all(i < j for i, j in zip(A, A[1:])) else "No")
