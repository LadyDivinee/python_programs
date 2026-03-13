#input numbers
input_numbers = []
#while True loop
while True:
    numbers = input("Enter a number: ")
    try:
        numbers = int(numbers)
        input_numbers.append(numbers)
    