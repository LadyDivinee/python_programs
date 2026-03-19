#collection method and input until invalid loop
from collections import Counter

numbers = []

while True:
    input_numbers = input("Enter numbers: ")
    try:
        input_numbers = int(input_numbers)
        numbers.append(input_numbers)
    except ValueError:
        print("Only integers allowed.")
        break

