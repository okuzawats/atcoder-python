h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = [[0 if c == "." else "#" for c in r] for r in s]

for i in range(h):
    for j in range(w):
        if s[i][j] != ".":
            continue
        for dx, dy in zip([-1, 0, 1, 1, 1, 0, -1, -1], [1, 1, 1, 0, -1, -1, -1, 0]):
            ni, nj = i + dx, j + dy
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if s[ni][nj] == "#":
                ans[i][j] += 1

for r in ans:
    print(*r, sep="")
