S, T = map(int, input().split())
ans = 0
for a in range(S + 1):
    for b in range(S + 1):
        for c in range(S + 1):
            if a + b + c <= S and a * b * c <= T:
                ans += 1
print(ans)
