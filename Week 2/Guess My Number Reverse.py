#Reverse Guess My Number
import random
import time

print("You have to choose a random number between 1 and 100.")
print("I will attempt to guess it.")

Nmbr = int(0)
Atmpts = int(5)
Guess = int(0)

Q_Loop = True
Chsn = False

while Q_Loop==True :             
    Query = input("\nDo you wish to play? [Y/N]")
    if Query=="Y" :
        while Chsn == False :
            Nmbr = int(input("\nOkay, pick a number: "))
            time.sleep(1)
            if Nmbr <= 0 :
                print("\nERROR! Invalid input, please try again!")
            if Nmbr > 100 :
                print("\nERROR! Invalid input, please try again!")
            if Nmbr > 0 :
                print("\nGot one? Okay!")
                Chsn = True
            
        Atmpts = int(input("\nHow many attempts should I have? "))
        time.sleep(1)
        while Guess != Nmbr :
            if Atmpts > 0 :
                print("\nAttempts remaining:", Atmpts)
                print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
                Guess = random.randint(1, 100)
                print("\nHow about...", Guess)
                def Load_slow(str):
                    for letter in str:
                        print(letter),
                        time.sleep(1)

                Load_slow("...")
                if Guess < 1 :
                    print("\nNumbers below 1 are not acceptable!")
                    Atmpts -= 1
                elif Guess > 100 :
                    print("\nNumbers above 100 are not acceptable!")
                    Atmpts -= 1
                elif Guess > Nmbr :
                    print("\nIt's a bit lower?")
                    Atmpts -= 1
                elif Guess < Nmbr :
                    print("\nIt's a bit higher?")
                    Atmpts -= 1

                if Guess == Nmbr :
                    print("\nWow, I guessed right! So the number was actually:", Nmbr)
                    Q_Loop = False
                    break

                if Atmpts <= 0 :
                    print("\nOh no! I've lost! The number was actually:", Nmbr)
                    Q_Loop = False
                    break
            
    elif Query=="y" :
        while Chsn == False :
            Nmbr = int(input("\nOkay, pick a number: "))
            time.sleep(1)
            if Nmbr <= 0 :
                print("\nERROR! Invalid input, please try again!")
            if Nmbr > 100 :
                print("\nERROR! Invalid input, please try again!")
            if Nmbr > 0 :
                print("\nGot one? Okay!")
                Chsn = True
            
        Atmpts = int(input("\nHow many attempts should I have? "))
        time.sleep(1)
        while Guess != Nmbr :
            if Atmpts > 0 :
                print("\nAttempts remaining:", Atmpts)
                print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
                Guess = random.randint(1, 100)
                print("\nHow about...", Guess)
                def Load_slow(str):
                    for letter in str:
                        print(letter),
                        time.sleep(1)

                Load_slow("...")
                if Guess < 1 :
                    print("\nNumbers below 1 are not acceptable!")
                    Atmpts -= 1
                elif Guess > 100 :
                    print("\nNumbers above 100 are not acceptable!")
                    Atmpts -= 1
                elif Guess > Nmbr :
                    print("\nIt's a bit lower?")
                    Atmpts -= 1
                elif Guess < Nmbr :
                    print("\nIt's a bit higher?")
                    Atmpts -= 1

                if Guess == Nmbr :
                    print("\nWow, I guessed right! So the number was actually:", Nmbr)
                    Q_Loop = False
                    break

                if Atmpts <= 0 :
                    print("\nOh no! I've lost! The number was actually:", Nmbr)
                    Q_Loop = False
                    break

    elif Query=="n" :
                print("\nUnderstandable have a nice day!\n")

                time.sleep(1)
                break        

    elif Query=="N" :
                print("\nUnderstandable have a nice day!\n")

                time.sleep(1)
                break

    else :
                 print("\nError! Invalid response!")

input("\n\nPress the enter key to exit")
