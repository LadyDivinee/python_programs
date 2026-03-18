#input numbers by the user
count = 0
for i in range (0,10):
    numbers = int(input(f"Enter number {i + 1}: "))

#check if even and print the result
    if numbers % 2 == 0:
        count += 1
print("The number of even numbers is", count)