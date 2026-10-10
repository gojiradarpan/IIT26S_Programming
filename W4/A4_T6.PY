print("Program starting.")
integer = int(input("Insert a positive integer: "))

count = 0
print(integer, end = "")
while integer != 1:
    if integer % 2 == 0:
        integer = integer // 2
    else:
        integer = (integer*3)+1
    print(f" -> {integer}", end="")

    count += 1

print()
print(f"Sequance had {count} total steps.")
print("\nProgram ending.")