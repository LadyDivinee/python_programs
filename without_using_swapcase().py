#string
word = "Dibayn Maangas"
result = ""
#swapcase
for ch in word:
    if ch == ch.lower():
        result += ch.upper()
    else:
        result += ch.lower()

print(result)
