#empty list and input numbers
numbers = []
for i in range(10):
    input_numbers = float(input(f"Enter number {i + 1}:"))
    numbers.append(input_numbers)
#to print the result
result = numbers[0]
for i in range (1,10):
    result -= numbers[i]
print(result)
