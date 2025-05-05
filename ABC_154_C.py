N = int(input())
A = [*map(int, input().split())]
print("YES" if len(A) == len(set(A)) else "NO")
