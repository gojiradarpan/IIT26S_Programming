print("Program starting.\n")
word_count=0
character_count=0
while True:
    word=input("Insert word (empty stops): ")
    if word == "":
        break
    word_count+=1
    character_count += len(word)
        
print("\nYou inserted:")
print(f"- {word_count} words")
print(f"- {character_count} characters")

print("\nProgram ending.")