#Food Combiner
import time

print("I'm going to ask you to enter two different favorite foods of yours",
      "\nAnd I'll combine them together.")

Food_01 = input("\nWhat is your most favorite food?")

Food_02 = input("\nWhat is your second most favorite food?")

print("\nCombining now!")

def Load_slow(str):
    for letter in str:
        print(letter),
        time.sleep(1)

Load_slow("...")

print("\nRESULTS!")
time.sleep(1)
print("\n",Food_01 + Food_02)

time.sleep(3)

print("\n\nThanks for using me!")

time.sleep(2)

input("Press the enter key to exit")
