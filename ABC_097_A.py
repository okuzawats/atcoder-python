A, B, C, D = map(int, input().split())
if abs(C - A) <= D:
    print("Yes")
elif abs(C - B) <= D and abs(B - A) <= D:
    print("Yes")
else:
    print("No")
