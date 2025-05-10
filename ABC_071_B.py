S = input()
not_used = list(set("abcdefghijklmnopqrstuvwxyz") - set(S))
print(min(not_used) if not_used else "None")
