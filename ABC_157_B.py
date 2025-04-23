A = []
for _ in range(3):
    for a in [*map(int, input().split())]:
        A.append(a)
N = int(input())
B = [int(input()) for _ in range(N)]

bingo = [A[i] in B for i in range(9)]
ans, y = "No", "Yes"
if bingo[0] and bingo[1] and bingo[2]:
    ans = y
elif bingo[3] and bingo[4] and bingo[5]:
    ans = y
elif bingo[6] and bingo[7] and bingo[8]:
    ans = y
elif bingo[0] and bingo[3] and bingo[6]:
    ans = y
elif bingo[1] and bingo[4] and bingo[7]:
    ans = y
elif bingo[2] and bingo[5] and bingo[8]:
    ans = y
elif bingo[0] and bingo[4] and bingo[8]:
    ans = y
elif bingo[2] and bingo[4] and bingo[6]:
    ans = y

print(ans)
