N, A = int(input()), [*map(int, input().split())]
print(
    "APPROVED" if all([a % 3 == 0 or a % 5 == 0 for a in A if a % 2 == 0]) else "DENIED"
)
