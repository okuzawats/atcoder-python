n = [c for c in input()]
print("Yes" if len(set(n[:2])) == 1 or len(set(n[1:])) == 1 else "No")
