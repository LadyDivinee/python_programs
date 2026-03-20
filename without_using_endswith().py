#strings
word = "helpful"
suffix = "ful"
#check the suffix if same
if word[-len(suffix):] == suffix:
    print("Same suffix")
else:
    print("Not same suffix")
