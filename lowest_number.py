#input numbers
input_numbers = []
#while True loop
while True:
    numbers = input("Enter number: ")
    try:
        numbers = int(numbers)
        input_numbers.append(numbers)
#ValueError for decimal or not a number
    except ValueError:
        print("Only integers are allowed.")
        break
#to print lowest number
if numbers:
    print("The lowest number is: ", min(input_numbers))