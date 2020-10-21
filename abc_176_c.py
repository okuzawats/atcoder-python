N = int(input())
A = map(int, input().split())
m, s = 0, 0
for a in A:
    m = max(m, a)
    s += m - a
print(s)
