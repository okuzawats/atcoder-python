N, K = map(int, input().split())
L = [*map(int, input().split())]
print(sum(sorted(L)[N - K :]))
