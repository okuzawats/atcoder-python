N, sum = input(), 0
for c in N:
    sum += int(c)
print("Yes" if int(N) % sum == 0 else "No")
