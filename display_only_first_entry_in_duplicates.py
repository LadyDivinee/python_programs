#input numbers
numbers = []
for i in range (10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
#check for duplicates
duplicates = set()
for num in numbers:
    if num not in duplicates:
        print(num)
        duplicates.add(num)

