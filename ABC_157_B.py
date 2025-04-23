A = []
for _ in range(3):
    for a in [*map(int, input().split())]:
        A.append(a)
N = int(input())
B = [int(input()) for _ in range(N)]

b = [False] * 9

for i in range(9):
    if A[i] in B:
        b[i] = True

if b[0] and b[1] and b[2]:
    print("Yes")
    exit()

if b[3] and b[4] and b[5]:
    print("Yes")
    exit()

if b[6] and b[7] and b[8]:
    print("Yes")
    exit()

if b[0] and b[3] and b[6]:
    print("Yes")
    exit()

if b[1] and b[4] and b[7]:
    print("Yes")
    exit()

if b[2] and b[5] and b[8]:
    print("Yes")
    exit()

if b[0] and b[4] and b[8]:
    print("Yes")
    exit()

if b[2] and b[4] and b[6]:
    print("Yes")
    exit()

print("No")
