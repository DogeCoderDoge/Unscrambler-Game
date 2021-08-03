#Introduction to game
#Random Number gen and array with words
#Check for correct answers
#Implement "You have - chances left" 


print("Welcome to Unscrambler! Type PLAY to continue! UPDATES to get an UPDATE LIST!")
start = input()
session_live = True
chancesLeft = 2 

if start == "PLAY":
    print("Which difficulty would you like? (EASY/HARD)")
    difficulty = input()

    while session_live:
        if difficulty == "EASY":
            import random
            wordNum = random.randint(0, 6)

            scrambledWords = ["lohle", "gamno", "praep", "rkanp", "treaw", "dngioc", "ptromi"]
            unscrambledWords = ["hello", "mango", "paper", "prank", "water", "coding", "import"]

            print("Unscramble this word:", scrambledWords[wordNum])
            answer = input()
            
            if answer == unscrambledWords[wordNum]:
                print("You answered correct!")
                
            elif answer != unscrambledWords[wordNum]:
                chancesLeft = chancesLeft - 1
                print("You have", chancesLeft, "chances left!")

                if chancesLeft == 0: 
                    print("You lost! Try again!")
                    session_live = False

        elif difficulty == "HARD":
            import random
            wordNum = random.randint(0, 2)

            scrambledWords = ["hcnkeci", "bkoeyrda", "mnaigza"]
            unscrambledWords = ["chicken", "keyboard", "amazing"]

            print("Unscramble this word:", scrambledWords[wordNum])
            answer = input()
            
            if answer == unscrambledWords[wordNum]:
                print("You answered correct!")
                
            elif answer != unscrambledWords[wordNum]:
                chancesLeft = chancesLeft - 1
                print("You have", chancesLeft, "chances left!")

                if chancesLeft == 0: 
                    print("You lost! Try again!")
                    session_live = False

        else:
            print(":/")
            session_live = False

elif start == "UPDATES":
    print("Update List- July 19th 2021: Added UPDATE list, Hard/Easy mode, fixed chances left/added chances system, added more words")

else:
    print(":/")