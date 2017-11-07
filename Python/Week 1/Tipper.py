#Tip Calculator
import time
print("Hello, this is the tip calculator for your bill.")
print("When prompted, please enter the requested values.")

time.sleep(1)

Food_01 = float(input("Total cost of your starter:£"))
              
Food_02 = float(input("Total cost of your main course:£"))
              
Food_03 = float(input("Total cost of your dessert:£"))
              
Drinks = float(input("Total cost of your drinks:£"))

print("\nThank you, calculating total.\n")

def Load_slow(str):
    for letter in str:
        print(letter),
        time.sleep(1)

Load_slow("...")

print("\nCalculation Complete!")
time.sleep(1)
Total = Food_01 + Food_02 + Food_03
print("\nTotal Cost: £", '%.2f' % Total)

Q_Loop = True

while Q_Loop==True :             
    Query = input("\nWould you like to calculate your tip? [Y/N]")
    if Query=="Y" :
                print("\nThank you, calculating tip at 15%.\n")

                def Load_slow(str):
                    for letter in str:
                        print(letter),
                        time.sleep(1)

                Load_slow("...")

                print("\nCalculation Complete!")
                time.sleep(1)
                Tip = (Total/100)*15
                print("\nTip Charged: £", '%.2f' % Tip)
                break

    elif Query=="y" :
                print("\nThank you, calculating tip at 15%.\n")
                def Load_slow(str):
                    for letter in str:
                        print(letter),
                        time.sleep(1)

                Load_slow("...")

                print("\nCalculation Complete!")
                time.sleep(1)
                Tip = (Total/100)*15
                print("\nTip Charged: £", '%.2f' % Tip)
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

