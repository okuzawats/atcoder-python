x, y, a = int(input()), 100, 0
while x > y:
    a += 1
    y += y // 100
print(a)
