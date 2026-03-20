#word and suffix
word = "helpful"
suffix = "ful"
#remove suffix and print output
if word[-len(suffix):] == suffix:
    result = word[:-len(suffix)]
else:
    result = word

print(result)
