from collections import defaultdict

N, K = map(int, input().split())
A = [*map(int, input().split())]

# Aの出現頻度をdictionaryに登録する。
bucket = defaultdict(int)
for i in A:
    bucket[i] += 1

# bucket.items()はKey/Valueのタプルを返す。
# このタプルに対して、Value(x[1])が小さい順にソートする。
# ここでKeyはボールに書かれている整数、Valueはその出現数である。
num = sorted(bucket.items(), key=lambda x: x[1])

# numの大きさ(size)がK以下の場合は、置き換える必要はない。
if len(num) <= K:
    print(0)
    exit()

# numのindexがKを超える部分について、その整数(Key)の出現数(Value)を足し合わせる。
cnt = 0
for i in range(len(num) - K):
    cnt += num[i][1]
print(cnt)
