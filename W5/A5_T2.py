def frameWord(PWord):
    length_star=len(PWord) + 4
    print("*" * length_star)
    print(f"* {PWord} *")
    print("*" * length_star)
    return None
    
def main():
    print("Program starting.")
    word = input("Insert word: ")
    print()
    frameWord(word)
    print("\nProgram ending.")
    return None

main()