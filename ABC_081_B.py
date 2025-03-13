n = int(input())
a = [*map(int, input().split())]

ans = 0
while all(i % 2 < 1 for i in a):
    ans += 1
    a = [i // 2 for i in a]
print(ans)
