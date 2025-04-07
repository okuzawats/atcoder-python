N = int(input())
T, A = map(int, input().split())
H = [*map(int, input().split())]

T = [abs(A - (T - H[i] * 0.006)) for i in range(N)]
print(T.index(min(T)) + 1)
