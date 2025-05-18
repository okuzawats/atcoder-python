A, B = map(int, input().split())

i = 0
while i * (A - 1) + 1 < B:
    i += 1

print(i)
