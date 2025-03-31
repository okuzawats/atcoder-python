n = int(input())

a = 0
for i in range(7):
    if 2**i <= n:
        a = i

print(2**a)
