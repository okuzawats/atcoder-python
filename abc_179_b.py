N = int(input())
f = 0
for _ in range(N):
    D = input().split()
    if D[0] == D[1]:
        f += 1
    else:
        f = 0
    if (f == 3):
        print('Yes')
        exit()
print('No')
