#input numbers list
input_numbers = []
#while True loop
while True:
    number = input("Enter a number: ")
    try:
        numbers = int(number)
        input_numbers.append(numbers)
#ValueError
    except ValueError:
        print("Only integers are allowed.")
        break