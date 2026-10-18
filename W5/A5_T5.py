
def options():
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")

def choice_1():
    word = input("Insert word: ")
    return word

def choice_2(word):
    print(f"Current word - \"{word}\"")

def choice_3(word):
    print(f"Word reversed - \"{word[::-1]}\"")

# def choice_0():
#     print("Exiting program.\nProgram ending.")
    

def main():
    print("Program starting.")
    options()
    w = ""
    
    while True:
        choice = input("Your choice: ")
        if choice == "1":
            w = choice_1()
            print()
            options()
            
        elif choice == "2":
            choice_2(w)
            print()
            options()
        elif choice == "3":
            choice_3(w)
            print()
            options()
        elif choice == "0":
            break
        else:
            print("Unknown option! Try again.")
            print()
            options()
    print("Exiting program.\n\nProgram ending.")
main()