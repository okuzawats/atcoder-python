n = int(input())
for i in range(1, n):
    if n <= i * (i + 1) // 2:
        print(i)
        break
