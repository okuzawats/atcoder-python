N = int(input())
A = [*map(int, input().split())]
A.sort()
print(A[-1] - A[0])
