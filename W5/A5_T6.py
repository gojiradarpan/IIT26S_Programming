def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        return -1

def show_count(count):
    print(f"Current count - {count}")

def increase_count(count):
    count += 1
    print("Count increased!")
    return count

def reset_count(count):
    count = 0
    print("Cleared count!")
    return count

def error_message():
    print("Unknown option!")

def main():
    print("Program starting.")
    count = 0
    while True:
        showOptions()
        c = askChoice()

        if c == 1:
            show_count(count)
            print()
                      
        elif c == 2:
            count = increase_count(count)
            print()

        elif c == 3:
            count = reset_count(count)
            print()

        elif c == 0:
            False
            break
        else:
            error_message()
            print()
    print("Exiting program.\n\nProgram ending.")    
            


main()