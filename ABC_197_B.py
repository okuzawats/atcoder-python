H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
S = [list(input()) for _ in range(H)]

ans = 0
if S[X][Y] == ".":
    ans += 1

for i in range(Y):
    if S[X][Y - 1 - i] == ".":
        ans += 1
    else:
        break

for i in range(1, W - Y):
    if S[X][Y + i] == ".":
        ans += 1
    else:
        break

for i in range(X):
    if S[X - 1 - i][Y] == ".":
        ans += 1
    else:
        break

for i in range(1, H - X):
    if S[X + i][Y] == ".":
        ans += 1
    else:
        break

print(ans)
