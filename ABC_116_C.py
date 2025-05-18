N = int(input())
H = [*map(int, input().split())]

ans, prev = 0, 0
for h in H:
    if prev < h:
        ans += h - prev
    prev = h

print(ans)
