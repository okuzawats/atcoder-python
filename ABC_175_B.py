N, L = int(input()), [*map(int, input().split())]
c = 0
for i in range(N):
    for j in range(i + 1, N):
        if L[i] == L[j]:
            continue
        for k in range(j + 1, N):
            if L[i] == L[k] or L[j] == L[k]:
                continue
            if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                c += 1
print(c)
