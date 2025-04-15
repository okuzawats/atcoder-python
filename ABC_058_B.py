O, E = input(), input()
S = [""] * (len(O + E))
S[::2], S[1::2] = O, E
print("".join(S))
