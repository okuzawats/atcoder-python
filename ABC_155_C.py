from collections import defaultdict

N, dict = int(input()), defaultdict(int)

for _ in range(N):
    dict[input()] += 1

max_value = max(dict.values())
max_pairs = {k: v for k, v in dict.items() if v == max_value}
for s in sorted(set(max_pairs)):
    print(s)
