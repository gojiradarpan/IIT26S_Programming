print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))
print()
if not start < stop:
    print("Starting point value must be less than the stopping point value.")

if not stop >= inspection >= start:
    print("Inspection value must be within the range of start and stop.")

if start < stop and start <= inspection <= stop:

    print("First loop - inspection with break:")
    first = True
    for i in range (start, stop):
        if i == inspection:
            break
        if first == False:
            print(" ", end="")
        print(i, end = "")
        first = False
    print()

    print("Second loop - inspection with continue:")
    first = True
    for i in range (start, stop):
        if i == inspection:
            continue
        if first == False:
            print(" ", end="")
        print(i, end="")
        first = False
    print()

print("\nProgram ending.")