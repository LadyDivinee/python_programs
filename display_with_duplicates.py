#input numbers
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
#check numbers with duplicates
duplicates = set()
for num in numbers:
    if numbers.count(num) > 1:
        duplicates.add(num)
for num in duplicates:
    print(num)