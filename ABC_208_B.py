from math import factorial

p, a = int(input()), 0

for i in range(10, 0, -1):
    f = factorial(i)
    while f <= p:
        a, p = a + 1, p - f

print(a)
