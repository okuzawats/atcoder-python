from math import floor

N = int(input())
price = floor(N * 1.08)

print("Yay!" if price < 206 else "so-so" if price == 206 else ":(")
