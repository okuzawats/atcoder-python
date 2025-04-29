N, L = int(input()), [2, 1]
for i in range(85):
    L.append(L[-1] + L[-2])
print(L[N])
