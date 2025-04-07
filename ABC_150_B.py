n, s = int(input()), input()
print(len([1 for i in range(n - 1) if s[i : i + 3] == "ABC"]))
