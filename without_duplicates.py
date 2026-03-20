#input loop
numbers = []

for i in range(10):
    input_number = float(input(f"Enter number {i + 1}: "))
    numbers.append(input_number)
#check the unique numbers and print output
unique_numbers = set(numbers)
for input_numbers in unique_numbers:
    if numbers.count(input_numbers) == 1:
        print(input_numbers)