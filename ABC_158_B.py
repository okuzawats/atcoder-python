N, A, B = map(int, input().split())

balls = []
while len(balls) <= N:
    balls += [1] * A + [0] * B
print(sum(balls[:N]))
