from collections import defaultdict

N = int(input())
A = [*map(int, input().split())]

dict = defaultdict(int)
for a in A:
    dict[a] += 1

cnt = 0
for k, v in dict.items():
    if k > v:
        cnt += v
    elif k < v:
        cnt += v - k

print(cnt)
