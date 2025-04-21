N, S = int(input()), []
for _ in range(N):
    s = input()
    S.append([len(s), s])
S.sort()

ans = ""
for s in S:
    ans += s[1]

print(ans)
