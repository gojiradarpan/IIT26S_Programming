print("Program starting.\n")
starting_point=int(input("Insert starting point: "))
stopping_point=int(input("Insert stopping point: "))
inspection_point=int(input("Insert inspection point: "))
if not starting_point < stopping_point:
    print("Starting point value must be less than the stopping point value.")
if not stopping_point >= inspection_point >= starting_point:
    print("Inspection value must be within the range of start and stop.")
print("\nFirst loop - inspection with break:")
for i in range(starting_point, inspection_point):
    if starting_point < inspection_point:
        print(starting_point, end=" ")
    else:
        print(starting_point)
    starting_point += 1
    if starting_point == inspection_point:
        break
for j in range(starting_point, stopping_point+1):
    if stopping_point < stopping_point:
        print(starting_point, end=" ")
    else:
        print(starting_point)
    if starting_point == inspection_point:
        continue