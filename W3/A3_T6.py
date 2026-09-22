print("Program staring.\n\nOptions:")
print("1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit")
choice = input("Your choice: ")

if choice == "1":
    celsius = float(input("Enter the amount of Celsius: "))
    c2f = ((1.8*celsius)+32)
    print(f"{celsius} °C equals to {round(c2f, 1)} °F")
elif choice == "2":
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    f2c = ((fahrenheit-32)/1.8)
    print(f"{fahrenheit} °F equals to {round(f2c, 1)} °C")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")