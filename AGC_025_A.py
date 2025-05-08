N = int(input())
ans = 10**18
for i in range(1, N):
    A, B = i, N - i
    sum_A = sum(int(x) for x in str(A))
    sum_B = sum(int(y) for y in str(B))
    ans = min(ans, sum_A + sum_B)
print(ans)
