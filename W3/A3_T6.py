print("Program starting.\nWelcome to the unit converter program!\nFollow the menu instructions below.\n\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = input("Your choice: ")
print("")
if choice == "1":
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice1 = input("Your choice: ")
    if choice1 == "1":
        m = float(input("Insert metres: "))
        km = m/1000
        print(f"{m} m is {round(km, 1)} km")
    elif choice1 == "2":
        km = float(input("Insert kilometres: "))
        m = km*1000
        print(f"{km} km is {round(m, 1)} m")
    elif choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice == "2":
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice2 = input("Your choice: ")
    if choice2 == "1":
        g = float(input("Insert grams: "))
        lbs = g * 0.002205
        print(f"{g} g is {round(lbs, 1)} lb")
    elif choice == "2":
        lbs = float(input("Insert pounds: "))
        g = lbs * 453.6
        print(f"{lbs} lb is {round(g, 1) g}")
    elif choice == "0":
        print("Exiting...")
    else:
        print("Unknown options.")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")