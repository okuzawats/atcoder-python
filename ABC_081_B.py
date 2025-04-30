N, A = int(input()), [*map(int, input().split())]
c = 0
while all(i % 2 < 1 for i in A):
    c += 1
    A = [i // 2 for i in A]
print(c)
