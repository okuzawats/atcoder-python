N, K = map(int, input().split())
H = sorted([int(input()) for _ in range(N)])

a = 10**9
for i in range(N - K + 1):
    a = min(a, H[i + K - 1] - H[i])
print(a)
