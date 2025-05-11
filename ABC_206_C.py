from collections import Counter
from functools import reduce

nc2 = lambda n: n * (n - 1) // 2
ttl = nc2(int(input()))
cnt = Counter([*map(int, input().split())]).values()
print(reduce(lambda acc, v: acc - nc2(v), cnt, ttl))
