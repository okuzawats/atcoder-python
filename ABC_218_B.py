P = [*map(int, input().split())]
C = [p + 96 for p in P]
print("".join(map(chr, C)))
