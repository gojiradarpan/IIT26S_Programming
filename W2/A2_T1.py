# Make a Python program, which prompts the user name and two floating numbers.
# Multiply the inserted numbers to get product. Round the product in two decimal precision.
# Complete the program output as shown below.

# Example program run:

# Program starting.
# What is your name: John
# Enter a floating point number: 3.1
# Enter second floating point number: 5.3
# John you gave numbers 3.1 and 5.3
# Multiplying first and second number will result in product 16.43
# Program ending.

print("Program starting.")
name = input("What is your name: ")
num_1 = float(input("Enter a floating point number: "))
num_2 = float(input("Enter second floating number point: "))
print(f"{name} you gave numbers {num_1} and {num_2}")
product = num_1 * num_2
product_2 = round(product, 2)
print(f"Multplyinug first and second number will result in product {product_2}")
print("Program ending.")