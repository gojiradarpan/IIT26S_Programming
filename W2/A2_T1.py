print("Program starting.")
name = input("What is your name: ")
num_1 = float(input("Enter a floating point number: "))
num_2 = float(input("Enter second floating number point: "))
print(f"{name} you gave numbers {num_1} and {num_2}")
product = num_1 * num_2
product_2 = round(product, 2)
print(f"Multplyinug first and second number will result in product {product_2}")
print("Program ending.")