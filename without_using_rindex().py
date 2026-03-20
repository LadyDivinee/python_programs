#word
word = "dibayn maangas"
#checks the index from the last character
for i in range(len(word)-1, -1, -1):
    if word[i] == "a":
        print(i)
        break
