#enter full name in incorrect casing
full_name = input("Enter full name in incorrect casing:")
#format in pascal casing
pascal_case = "".join(full_name.title().split())
print(pascal_case)