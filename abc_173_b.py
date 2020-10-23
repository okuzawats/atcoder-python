a = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
N = int(input())
for _ in range(N):
    a[input()] += 1
for k, v in a.items():
    print('{} x {}'.format(k, v))
