# N, M = map(int, input().split())
# S = [[*map(int, input().split())] for _ in range(M)]

# for i in range(10 ** (N - 1), 10**N):
#     num = str(i)
#     for s, c in S:
#         print(num[s - 1], type(num[s - 1]), str(c), type(str(c)))
#         if num[s - 1] != str(c):
#             break
#         else:
#             print(i)
#             exit()
