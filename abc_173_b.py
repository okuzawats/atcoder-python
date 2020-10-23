s = [input() for _ in range(int(input()))]
for k in ['AC', 'WA', 'TLE', 'RE']:
    print(k, 'x', s.count(k))
