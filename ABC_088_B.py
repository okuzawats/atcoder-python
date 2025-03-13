n = int(input())
a = [*map(int, input().split())]
a.sort(reverse=True)
print(sum([a[i] if i % 2 < 1 else -a[i] for i in range(n)]))
