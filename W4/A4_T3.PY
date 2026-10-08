print("Program starting.\n")
starting_value=int(input("Insert starting value: "))
ending_value=int(input("Insert ending value: "))

while starting_value <= ending_value:
    if starting_value < ending_value:
        print(starting_value, end=" ")
    else:
        print(starting_value)
    starting_value+=1
print("\nProgram ending.")