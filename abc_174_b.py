N, D = map(int, input().split())
c = 0
for i in range(N):
    X, Y = map(int, input().split())
    if X**2 + Y**2 <= D**2:
        c += 1
print(c)
