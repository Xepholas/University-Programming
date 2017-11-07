#Guess My Number
import random
import time

print("A random number between 1 and 100 will be chosen.")
print("You have 5 attempts to guess this number.")

Nmbr = int(0)
Atmpts = int(5)
Guess = int(0)

Q_Loop = True

while Q_Loop==True :             
    Query = input("\nDo you wish to play? [Y/N]")
    if Query=="Y" :
                print("\nLet me think...\n")

                def Load_slow(str):
                    for letter in str:
                        print(letter),
                        time.sleep(1)

                Load_slow("...")

                print("\nOkay, number chosen!")
                time.sleep(1)
                Nmbr = random.randint(1,100)

                while Guess != Nmbr :
                    if Atmpts > 0 :
                        print("\nAttempts remaining:", Atmpts)
                        print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
                        Guess = int(input("What do you think it may be? "))

                        if Guess < 1 :
                            print("\nNumbers below 1 are not acceptable!")
                            Atmpts -= 1
                        elif Guess > 100 :
                            print("\nNumbers above 100 are not acceptable!")
                            Atmpts -= 1
                        elif Guess > Nmbr :
                            print("\nLook a bit lower...")
                            Atmpts -= 1
                        elif Guess < Nmbr :
                            print("\nLook a bit higher...")
                            Atmpts -= 1
                        
                    if Guess == Nmbr :
                        print("\nCongrats you guessed right! The number was:", Nmbr)
                        Q_Loop = False
                        break

                    if Atmpts <= 0 :
                        print("\nGame Over! The number was:", Nmbr)
                        Q_Loop = False
                        break
            
    elif Query=="y" :
                print("\nLet me think...\n")

                def Load_slow(str):
                    for letter in str:
                        print(letter),
                        time.sleep(1)

                Load_slow("...")

                print("\nOkay, number chosen!")
                time.sleep(1)
                Nmbr = random.randint(1,100)

                while Guess != Nmbr :
                    if Atmpts > 0 :
                        print("\nAttempts remaining:", Atmpts)
                        print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
                        Guess = int(input("What do you think it may be? "))

                        if Guess < 1 :
                            print("\n\nNumbers below 1 are not acceptable!")
                            Atmpts -= 1
                        elif Guess > 100 :
                            print("\n\nNumbers above 100 are not acceptable!")
                            Atmpts -= 1
                        elif Guess > Nmbr :
                            print("\n\nLook a bit lower...")
                            Atmpts -= 1
                        elif Guess < Nmbr :
                            print("\n\nLook a bit higher...")
                            Atmpts -= 1
                        
                    if Guess == Nmbr :
                        print("\nCongrats you guessed right! The number was:", Nmbr)
                        Q_Loop = False
                        break

                    if Atmpts <= 0 :
                        print("\nGame Over! The number was:", Nmbr)
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
