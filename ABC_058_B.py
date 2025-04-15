O, E = input(), input()

S = [""] * (len(O + E))
S[::2] = O
S[1::2] = E
print("".join(S))
