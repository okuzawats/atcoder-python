N, X = map(int, input().split())
A = sorted([*map(int, input().split())])

cnt = 0
for a in A:
    if X - a >= 0:
        cnt += 1
        X -= a

ans = cnt - 1 if X > 0 else cnt
print(ans)
