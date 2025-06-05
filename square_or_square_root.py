# Square or Square root number
import math

number = float(input("Enter number:"))

user_input = int(input("Type 1-square or type 2-square root:"))

if user_input == 1:
    number_squared = number**2
    print(f"The square of number you type is: {number_squared}")
elif user_input == 2:
    number_squared_root = math.sqrt(number)
    print(f"The square root of number you type is: {number_squared_root}")
else:
    print("Invalid input!")