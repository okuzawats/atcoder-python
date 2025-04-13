P = [*map(int, input().split())]
S = ""
for i in P:
    S += chr(i + 96)
print(S)
