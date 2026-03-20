#string
word = "DIBAYN MAANGAS"
#translation table
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "abcdefghijklmnopqrstuvwxyz"
translation_table = str.maketrans(uppercase, lowercase)
#print in lowercasing
word_in_lowercase = word.translate(translation_table)
print(word_in_lowercase)