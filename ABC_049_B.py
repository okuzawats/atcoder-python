H, W = map(int, input().split())
C = [input().split() for _ in range(H)]
for w in C:
    s = " ".join(w)
    print(f"{s}\n{s}")
