k = int(input())
a, b = [*map(int, input().split())]

ng = all(i % k > 0 for i in range(a, b + 1))
print("NG" if ng else "OK")
