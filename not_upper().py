#fixed string
name = "dibayn.mngs"
#translation table
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
translation_table = str.maketrans(lower_case, upper_case)
#capitalizing letters
name_in_capitalized = name.translate(translation_table)
#print the output
print(name_in_capitalized)
