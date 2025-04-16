S, T = input(), input()
print("Yes" if "".join(sorted(S)) < "".join(sorted(T, reverse=True)) else "No")
