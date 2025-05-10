S = input()
not_used = sorted(list(set("abcdefghijklmnopqrstuvwxyz") - set(S)))
print(not_used[0] if not_used else "None")
