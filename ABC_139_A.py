S, T = input(), input()
print(len([1 for s, t in zip(S, T) if s == t]))
