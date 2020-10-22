N, D = map(int, input().split())
c = 0
for _ in range(N):
    X, Y = map(int, input().split())
    c += X*X + Y*Y <= D*D
print(c)
