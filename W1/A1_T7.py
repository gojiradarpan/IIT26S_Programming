print("Calculate fuel consumption.")
Feed = input("Enter travel distance (kilometres): ")
Distance = int(Feed)
Feed = input("Enter fuel usage (litres): ")
FuelUsage = int(Feed)
Feed = (FuelUsage / Distance) * 100
Consumption = int(Feed)
print(f"Fuel consumption is {Consumption} l per 100 km")
