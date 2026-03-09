#input numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
#to show the numbers between two numbers
for i in range(num2 - num1 -1):
    num1 += 1
    print(num1)