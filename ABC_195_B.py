A, B, W = map(int, input().split())
m, M = 1e9, 0
for n in range(1, 1000001):
    if A * n <= 1000 * W <= B * n:
        m, M = min(m, n), max(M, n)
print(m, M) if M != 0 else print("UNSATISFIABLE")
