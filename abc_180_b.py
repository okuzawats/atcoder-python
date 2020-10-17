N = int(input())
x = input().split()
a, b = [], []
for y in x:
    a.append(abs(int(y)))
    b.append(int(y) ** 2)
print(sum(a))
print(sum(b) ** 0.5)
print(max(a))
