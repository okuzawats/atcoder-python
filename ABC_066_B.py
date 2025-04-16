S = input()
for i in range(len(S) - 2, 1, -2):
    if S[: i // 2] == S[i // 2 : i]:
        print(i)
        exit()
