def askName():
    name=input("Insert name: ")
    return name

def greetUser(PName):
    print(f"Hello {PName}!")
    return None

def main():
    print("Program starting.")
    name = askName() #this variable name is not related (independent) to  variable "name" from line 2
    greetUser(name) #this call parameter "name" should be the same variable named in line 11
    print("Program ending.")
    return None

main()