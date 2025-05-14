A, B, C, D = map(int, input().split())
L, R = A + B, C + D
print("Left" if L > R else "Right" if L < R else "Balanced")
