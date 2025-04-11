N = int(input())
P = sorted([int(input()) for _ in range(N)])
print(sum(P) - P[-1] // 2)
