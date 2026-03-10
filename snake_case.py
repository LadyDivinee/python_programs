#input full name in incorrect casing
full_name = input("Enter full name in incorrect casing: ")
#formatting to snake case
snake_case = "_".join(full_name.lower().split())
print(snake_case)