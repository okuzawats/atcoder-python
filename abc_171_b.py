N, K = map(int, input().split())
print(sum(sorted(list(map(int, input().split())))[:K]))
