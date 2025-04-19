N = int(input())
for i in range(26):
    for j in range(15):
        if N == i * 4 + j * 7:
            print("Yes")
            exit()
print("No")
