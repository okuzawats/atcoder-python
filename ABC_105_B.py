N = int(input())
S = set([i * 4 + j * 7 for i in range(26) for j in range(15)])
print("Yes" if N in S else "No")
