from itertools import combinations
N = int(input())
L = [*map(int, input().split())]
c = 0
for x, y, z in combinations(L, 3):
    if x == y or y == z or z == x:
        continue
    if x + y <= z or y + z <= x or z + x <= y:
        continue
    c += 1
print(c)
