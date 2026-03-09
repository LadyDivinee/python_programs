#using set() to maintain unique numbers
no_duplicate_numbers = set()
#for loop
for i in range (10):
    numbers = float(input(f"Enter number {i + 1}: "))
#.add to add the numbers in the set
    no_duplicate_numbers.add(numbers)
print(no_duplicate_numbers)