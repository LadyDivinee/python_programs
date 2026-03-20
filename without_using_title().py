#string
name = "DIBAYN MAANGAS"
#split text
text = name.split()
result = ""
#convert to title case
for word in text:
    result += word[0].upper() + word[1:].lower() + " "

result = result.rstrip()

print(result)