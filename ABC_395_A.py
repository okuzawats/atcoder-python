n = int(input())
a = [*map(int, input().split())]

ans = all(i < j for i, j in zip(a, a[1:]))
print("Yes" if ans else "No")
