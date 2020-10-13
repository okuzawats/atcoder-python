N = int(input())
v = []
for i in range(N):
    v.append(input().split())
f = False
for i in range(N - 2):
    if v[i][0] == v[i][1] and v[i+1][0] == v[i+1][1] and v[i+2][0] == v[i+2][1]:
        f = True
        break
if f:
    print('Yes')
else:
    print('No')
