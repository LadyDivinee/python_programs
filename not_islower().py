#fixed string
name = "dibayn"
#lower case and upper case string
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#check if in lower case
lower = True
for ch in name:
    if ch in lower_case:
        lower = False
        break