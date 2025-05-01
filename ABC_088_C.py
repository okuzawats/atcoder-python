C = [[*map(int, input().split())] for _ in range(3)]

S1 = C[0][0] + C[1][1] + C[2][2]
S2 = (C[0][1] + C[1][2] + C[2][0] + C[0][2] + C[2][1] + C[1][0]) // 2
print("Yes" if S1 == S2 else "No")
