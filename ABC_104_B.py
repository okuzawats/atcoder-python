s = input()

a = s[0] == "A"
b = s[2 : len(s) - 1].count("C") == 1
c = sum(map(str.isupper, s)) == 2

print("AC" if a and b and c else "WA")
