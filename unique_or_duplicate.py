#input numbers
input_numbers = []
#while True loop
while True:
    numbers = input("Enter number: ")

    try:
        numbers = int(numbers)

        if numbers in input_numbers:
            print ("Duplicate")
        else:
            print("Unique")
        input_numbers.append(numbers)
