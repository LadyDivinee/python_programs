#fixed string
name = "dibayn"
#lower case and upper case string
lower_case = "abcdefghijklmnopqrstuvwxyz"
#check if in lower case
lower = True
for ch in name:
    if ch not in lower_case:
        lower = False
        break
#print output
if lower:
    print("All in lower case.")
else:
    print("Not all in lower case.")