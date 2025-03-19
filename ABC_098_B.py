n = int(input())
s = input()

a = 0
for i in range(1, n):
    x, y = s[:i], s[i:]
    a = max(a, len(set(x) & set(y)))

print(a)
