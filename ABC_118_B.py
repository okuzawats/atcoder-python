N, M = map(int, input().split())
bucket, ans = [0] * M, 0

for i in range(N):
    for a in [*map(int, input().split())][1:]:
        bucket[a - 1] += 1

for b in bucket:
    if b == N:
        ans += 1

print(ans)
