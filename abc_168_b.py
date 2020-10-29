K = int(input())
S = input()
if len(S) <= K:
    print(S)
else:
    print('{}...'.format(S[:K]))
