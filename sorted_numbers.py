#input numbers
input_numbers = []
#while True loop
while True:
    numbers = input("Enter a number: ")
    try:
        numbers = int(numbers)
        input_numbers.append(numbers)
#ValueError for decimal and not a number
    except ValueError:
        print("Only integers are allowed.")
        break
#print in ascending order
if numbers:
    print("The numbers in ascending order are", sorted(input_numbers))