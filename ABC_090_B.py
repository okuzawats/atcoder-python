a, b = map(int, input().split())
print(len([1 for i in range(a, b + 1) if str(i) == str(i)[::-1]]))
