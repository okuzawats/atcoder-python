N = int(input())
L = [*map(int, input().split())]
c = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                continue
            elif L[i] + L[j] <= L[k] or L[j] + L[k] <= L[i] or L[k] + L[i] <= L[j]:
                continue
            else:
                c += 1
print(c)
