#string
word = "disagree"
prefix = "dis"
#check the prefix and print the result
if word[:len(prefix)] == prefix:
    result = word[len(prefix):]
else:
    result = word

print(result)
