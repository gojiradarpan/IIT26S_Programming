print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

if not start < stop:
    print("Starting point value must be less than the stopping point value.")

if not stop >= inspection >= start:
    print("Inspection value must be within the range of start and stop.")

if start < stop and start <= inspection <= stop:

    print("\nFirst loop - inspection with break:")
    for i in range (start, stop):
        if i == inspection:
            break
        if i < inspection-1:
            print(i, end = ".")
        else:
            print(i)

    print("Second loop - inspection with continue:")
    for i in range (start, stop):
        if i == inspection:
            continue
        if i < stop-1:
            print(i, end = ".")
        else:
            print(i)


print("\nProgram ending.")