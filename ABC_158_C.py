a, b = map(int, input().split())

for i in range(1, 1001):
    if a == int(i * 0.08) and b == int(i * 0.1):
        print(i)
        exit()

print(-1)
