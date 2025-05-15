from collections import defaultdict

N, d, c = int(input()), defaultdict(int), 0

for a in [*map(int, input().split())]:
    d[a] += 1
for k, v in d.items():
    c += v - k if k <= v else v
print(c)
