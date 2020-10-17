N = int(input())
a = []
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        a.append(i)
        if i != N // i:
            a.append(N // i)
a.sort()
for i in a:
    print(i)
