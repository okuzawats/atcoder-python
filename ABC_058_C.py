N = int(input())
S = [input() for _ in range(N)]
count_min = [10**18] * 26

for s in S:
    count_s = [0] * 26
    for c in s:
        count_s[ord(c) - 97] += 1
    for i in range(26):
        count_min[i] = min(count_min[i], count_s[i])

ans = ""
for i in range(26):
    ans += chr(i + 97) * count_min[i]
print(ans)
