DELIMITER = ","

def collectWords():
    print("Program starting.")
    words=""
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        if words == "":
            words = word
        else:
            words = words + DELIMITER + word
    return words

def analyseWords():
    word = collectWords()
    listed_word = word.split(",")
    num_of_words = len(listed_word)
    num_of_char = 0
    for word in listed_word:
        num_of_char = num_of_char + len(word)
    Avg = num_of_char / num_of_words

    print("- {:} Words".format(num_of_words))
    print("- {:} Characters".format(num_of_char))
    print("- {:.2f} Average word length".format(Avg))
    print("Program ending.")

analyseWords()