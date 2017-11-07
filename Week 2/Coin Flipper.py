#Coin flipper (x100)
import random
import time

print("This program simulates the flipping of a coin 100 times.")

Heads = 0
Tails = 0
Q_Loop = True

while Q_Loop==True :             
    Query = input("\nWould you like to continue? [Y/N]")
    if Query=="Y" :
                print("\nFlipping coin...\n")

                def Load_slow(str):
                    for letter in str:
                        print(letter),
                        time.sleep(1)

                Load_slow("...")

                print("\nCoin flips complete!")
                time.sleep(1)
                Flip = 0
                while Flip < 100  :
                    Result = random.randint(1, 2)
                    if Result == 1 :
                        Heads += 1
                        Flip +=1
                    elif Result == 2:
                        Tails += 1
                        Flip+=1

                print("\nResults:")
                print("\nHeads:", Heads)
                print("\nTails:", Tails)
                break
            
    elif Query=="y" :
                print("\nFlipping coin...\n")
                def Load_slow(str):
                    for letter in str:
                        print(letter),
                        time.sleep(1)

                Load_slow("...")

                print("\nCoin flips complete!")
                time.sleep(1)
                Flip = 0
                while Flip < 100  :
                    Result = random.randint(1, 2)
                    if Result == 1 :
                        Heads += 1
                        Flip +=1
                    elif Result == 2:
                        Tails += 1
                        Flip+=1

                print("\nResults:")
                print("\nHeads:", Heads)
                print("\nTails:", Tails)
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
