N, M = map(int, input().split())
c, s = 0, 0
for a, b in sorted([[*map(int, input().split())] for _ in range(N)]):
    for i in range(b):
        c, s = c + 1, s + a
        if c == M:
            print(s)
            exit()
