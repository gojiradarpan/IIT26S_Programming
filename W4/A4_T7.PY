print("Program starting.\n")

print("Check multiplicative persistence.")
integer=int(input("Insert an integer: "))
str_integer = str(integer)

count = 0

while int(str_integer) >= 10:

    x = 1
    first = True

    for i in str_integer:
        if first == False:
            print(" * ", end="")
        print(i, end="")
        first = False
        x = x*int(i)
    print(f" = {x}")
    count += 1
    str_integer = str(x)

print("No more steps.")

print(f"\nThis program took {count} step(s)")

print("\nProgram ending.")