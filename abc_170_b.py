X, Y = map(int, input().split())
print(['No', 'Yes'][Y % 2 == 0 and X * 2 <= Y <= X * 4])
