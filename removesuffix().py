#fixed string
name = "dibayn.mngs"
suffix = ".mngs"
#index of the suffix
index = len(name) - len(suffix)
#check the suffix
if name [index:] == suffix:
    just_name = name[:index]
else:
    just_name = name
    