total = 0
for i in range(10):
#input
    numbers = float(input(f"Enter the number {i+1}:"))
#for the total of numbers
    total += numbers
#print the sum of 10 numbers
print(f"The sum of 10 numbers is {total}")