N = int(input())
A = list(map(int, input().split()))
if 0 in A:
    print(0)
    exit()
acc = 1
for a in A:
    acc *= a
    if acc > 1000000000000000000:
        print(-1)
        exit()
print(acc)
