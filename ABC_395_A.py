n = int(input())
a = list(map(int, input().split()))

ans = True
for i in range(n-1):
    if a[i] < a[i+1]:
        continue
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
