A, B = map(int, input().split())
can = A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0
print("Possible" if can else "Impossible")
