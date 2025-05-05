N, M = map(int, input().split())
buc = [0] * M
for i in range(N):
    for a in [*map(int, input().split())][1:]:
        buc[a - 1] += 1
print(len([b for b in buc if b == N]))
