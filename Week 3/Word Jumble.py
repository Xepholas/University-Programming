#Word Jumble 2.0
import random

Game = True
Score = int(0)
Words = ("python", "testing", "guessing", "programming", "answer")

while Game == True :
    word = random.choice(Words)
    correct = word
    point = True
    attempts = int(5)
    jumble = ""

    while word :
        position = random.randrange(len(word))
        jumble += word [position]
        word = word[:position] + word[(position + 1):]

#Game Start

    print("\nThe jumble is: ", jumble)
    print("Number of guesses remaining: ", attempts)
    if correct == "python" :
        Hint = "The language used to make this!"
    elif correct == "testing" :
        Hint = "Word for making sure something works."
    elif correct == "guessing" :
        Hint = "What you are doing right now."
    elif correct == "programming" :
        Hint = "What was done to make this game."
    elif correct == "answer" :
        Hint = "Something you need to give"

    print("Current score:", Score)
    guess = input("\nWhat do you think it is? ")
    attempts -= 1

    while guess != correct and guess != "" and attempts > 0 :
        print("\nThat's not it!")

        x = input("\nWould you like a hint? Be careful, you won't get a point this game if you do so! [Y/N] ")

        if x == "y" :
            print("\nHint:", Hint)
            point = False
        elif x == "Y" :
            print("\nHint:", Hint)
            point = False  
        elif x == "n" :
            print("\nOkay, good luck!")
        elif x == "N" :
            print("\nOkay, good luck!")
        print("Current score:", Score)    
        print("\nNumber of guesses remaining: ", attempts)
        guess = input("\nWhat do you think it is? ")
        attempts -= 1

    if guess == correct :
        print("\nCongrats, the word was:", correct)
        if point == True :
            Score +=1
            print("\nAs you used no hints, you've gained a point!")
            print("\nYour score is now:", Score)
        elif point == False :
            print("\nAs you used a hint, you've gained no points!")

        print("Thanks for playing!")

        play = input("Would you like to play again? [Y/N] ")

        if play == "y" :
            print("")
        elif play == "Y" :
            print("")
        elif play == "n" :
            print("\nGoodbye!")
            Game = False
        elif play == "N" :
            print("\nGoodbye!")
            Game = False
            


    if attempts == 0 :
        print("\nGame Over")
        print("\nThe word was:", correct)

        play = input("Would you like to play again? [Y/N] ")

        if play == "y" :
            print("")
        elif play == "Y" :
            print("")
        elif play == "n" :
            print("\nGoodbye!")
            Game = False
        elif play == "N" :
            print("\nGoodbye!")
            Game = False

input("\n\nPress enter to exit.")
