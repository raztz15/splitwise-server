def hangman(word):
    wrong = 0
    stages = [
        "",
        "_______________",
        "|",
        "|                  |   ",
        "|                  0   ",
        "|                 /|\  ",
        "|                  |   ",
        "|                 / \  ",
        "|"
        ]

    # tracking characters are eft to find
    # word = list of characters
    remaining_letters = list(word)
    # the underscore represents each character that the word contains
    board = ["___"] * len(word)
    # win = True or False if the winner wins or lose obviously
    win = False
    print("Hello to Hangman")

    while wrong < len(stages) -1:
        # print a blank space just for aesthetics
        print("\n")
        msg = "Guess the word"
        char = input(msg)
        # now we're checking if the player guesses right one of the letters
        if char in remaining_letters:
            # using the index function to put the character in the right place in the list
            cind = remaining_letters.index(char)
            #  putting the char in the board
            board[cind] = char
            remaining_letters[cind] = "$"
