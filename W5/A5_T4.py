def askDimension(PPrompt: str) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

# Width = askNumber("width")
# Height = askNumber("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight
   return Area

def main():
   print("Program starting.")
   Width = askDimension("width")
   Height = askDimension("height")
   print()
   Area = calcRectangleArea(Width, Height)
   print(f"Area is {Area}²")
   print("Program ending.")
   return None

main()