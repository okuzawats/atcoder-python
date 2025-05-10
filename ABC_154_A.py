S, T = input().split()
A, B = map(int, input().split())
U = input()

dict = {S: A, T: B}
dict[U] -= 1

print(dict[S], dict[T])
