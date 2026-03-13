#input numbers
input_numbers = []
#while true loop
while True:
    numbers = input("Enter a number: ")
    try:
        numbers = int(numbers)
        input_numbers.append(numbers)
#ValueError
    except ValueError:
        print("Only integers are allowed.")
        break
#print the highest number
if numbers:
    print("The highest number is: ", max(input_numbers))
