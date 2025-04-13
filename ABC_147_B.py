S = input()
print(sum([1 if S[i] != S[len(S) - 1 - i] else 0 for i in range(len(S) // 2)]))
