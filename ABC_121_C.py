N, M = map(int, input().split())
AB = [[*map(int, input().split())] for _ in range(N)]
AB.sort()

c, sum = 0, 0
for ab in AB:
    a = ab[0]
    for i in range(ab[1]):
        c += 1
        sum += a
        if c == M:
            print(sum)
            exit()
