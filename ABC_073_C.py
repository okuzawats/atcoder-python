from collections import defaultdict

N, dict = int(input()), defaultdict(bool)
for _ in range(N):
    a = int(input())
    dict[a] = not dict[a]
print(len([0 for b in dict.values() if b == True]))
