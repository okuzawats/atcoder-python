from collections import defaultdict

N = int(input())
A = [*map(int, input().split())]
dct, cnt = defaultdict(int), 0

for a in A:
    mod = a % 200
    cnt += dct[mod]
    dct[mod] += 1
print(cnt)
