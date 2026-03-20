#string and letters in uppercase
name = "DIBAYN MAANGAS"

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upper = True
#check if all in uppercase
for ch in name:
    if ch.isalpha() and ch not in uppercase:
        upper = False
if upper:
    print("All in uppercase.")
else:
    print("Not all in uppercase.")
