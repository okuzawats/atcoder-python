N = int(input())
S = [input() for _ in range(N)]
T = [[0] * N for _ in range(26)]

for i in range(N):
    for j in range(26):
        # i=0 => S1, ..., i=N-1 => Sn
        # j=0 => a, ..., j=25 => z
        # a~zそれぞれについて、Snに何文字含まれているかをカウントする。
        T[j][i] = S[i].count(chr(j + 96))

str = ""
for i in range(26):
    # 最も出現回数の少なかった回数分、文字を連結する。
    str += chr(i + 96) * min(T[i])
print(str)
