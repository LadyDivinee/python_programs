#input text with spaces in the beginning
text = input("Enter text with spaces at the beginning: ")

result = ""
spaces = False
#to remove the spaces at the beginning
for ch in text:
    if ch != " ":
        spaces = True
    if spaces:
        result += ch

print (result)

