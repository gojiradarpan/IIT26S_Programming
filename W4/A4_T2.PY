print("Program starting.\n")
starting_value=int(input("Insert starting value: "))
stopping_value=int(input("Insert stopping value: "))
print("\nStarting for-loop:")
for i in range(starting_value, stopping_value+1):
    if i < stopping_value:
        print(i, end=" ")
    else:
        print(i)
print("\nProgram ending.")