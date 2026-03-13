#fixed string with spaces
name = "dibayn.mngs    "
#check the index of the space to remove spaces
if name[-1] == " ":
    just_name = name[:-1]
else:
    just_name = name
