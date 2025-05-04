from functools import reduce

A, B, C, X, Y = map(int, input().split())

print(
    reduce(
        lambda acc, c: min(
            acc, max(0, X - c // 2) * A + max(0, Y - c // 2) * B + c * C
        ),
        range(max(X, Y) * 2 + 1),
        10**18,
    )
)
