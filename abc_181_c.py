from itertools import combinations
N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
for p1, p2, p3 in combinations(P, 3):
    if (p3[1] - p1[1]) * (p2[0] - p1[0]) == (p2[1] - p1[1]) * (p3[0] - p1[0]):
        print('Yes')
        exit()
print('No')
