from collections import Counter
from functools import reduce

N = int(input())
A = [*map(int, input().split())]
c = reduce(lambda acc, a: acc - a * (a - 1) // 2, Counter(A).values(), N * (N - 1) // 2)
print(c)
