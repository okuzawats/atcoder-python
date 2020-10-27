N = int(input())
A = map(int, input().split())
acc = 1
for a in A:
    acc *= a
if acc > 10 ** 18:
    print(-1)
else:
    print(acc)
