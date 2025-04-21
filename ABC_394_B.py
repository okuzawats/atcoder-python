N = int(input())
S = [input() for _ in range(N)]
S.sort(key=len)
print("".join(S))
