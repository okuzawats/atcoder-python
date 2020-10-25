X, Y = map(int, input().split())
print(['No', 'Yes'][Y % 2 == 0 and Y >= X * 2 and Y <= X * 4])
