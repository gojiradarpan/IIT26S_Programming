print("Program staring.\nString comparisions")
word = input("Insert first word: ").lower()
character = input("Insert a character: ").lower()
if character in word:
    print(f"Word \"{word}\" contains character \"{character}\"")
else:
    print(f"Word \"{word}\" doesn't contain character \"{character}\"")
word2 = input("Insert second word: ").lower()
if word == word2:
    print(f"Both inserted words are the same alphabetically, \"{word}\"")
elif word < word2:
    print(f"The first word \"{word}\" is before the second word \"{word2}\" alphabetically.")
else:
    print(f"The second word \"{word2}\" is before the first word \"{word}\" alphabetically.")
print("Program ending.")