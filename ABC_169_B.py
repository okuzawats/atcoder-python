from functools import reduce

N = int(input())
A = [*map(int, input().split())]

m = reduce(lambda acc, x: acc * x, A[1:], A[0])
print(m if m <= 10**18 else -1)
