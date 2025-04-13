import re

A, B = map(int, input().split())
S = input()

print("Yes" if re.match(f"^[0-9]{{{A}}}-?[0-9]{{{B}}}$", S) else "No")
