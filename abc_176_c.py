N = int(input())
A = map(int, input().split())
s = 0
p = 10 ** 9
for a in A:
    if a > p:
        s += a - p
    p = a
print(s)
