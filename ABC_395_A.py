n = int(input())
a = [*map(int, input().split())]

ans = True
for i in range(n-1):
    if a[i] < a[i+1]:
        continue
    else:
        ans = False
        break

print('Yes' if ans else 'No')
