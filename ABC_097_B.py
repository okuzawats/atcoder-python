x = int(input())

limit = int(x**0.5 + 1)
a = 1
for b in range(1, limit):
    for p in range(1, limit):
        n = b**p
        if n > x:
            break
        a = max(a, n)

print(a)
