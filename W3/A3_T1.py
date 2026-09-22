# Program starting.
# Insert two integers.
# Insert first integer: 5
# Insert second integer: 5
# Comparing inserted integers.
# Integers are the same

# Adding integers together
# 5 + 5 = 10

# Checking the parity of the sum...
# Sum is even.
# Program ending.

print("Program staring.")
print("Insert two integers.")
int1 = int(input("Enter first integer: "))
int2 = int(input("Enter second integer: "))
print("Comparing inserted integers.")
if int1 > int2:
    print("First integer is greater.")
elif int1 < int2:
    print("Second integer is greater.")
else:
    print("Integers are the same")
print("")
print("Adding integers together")
sum = (int1 + int2)
print(f"{int1} + {int2} = {sum}")
print("")
print("Checking the parity of the sum...")
if sum % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")