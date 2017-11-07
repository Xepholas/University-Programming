#Fortune Generator
import time
import random

print("\nWelcome! This program in a moment will generate one of five random fortunes for you...")
time.sleep(1)
print("\nUh... I mean your fortune will be divined here and now!")
time.sleep(1)
print("\nWell, here we go!")
    
def Load_slow(str):
    for letter in str:
        print(letter),
        time.sleep(1)

Load_slow("...")

fortune = random.randint(1, 5)

if fortune == 1 :
    print("Fortune 1")

elif fortune == 2 :
    print("Fortune 1")

elif fortune == 3 :
    print("Fortune 1")

elif fortune == 4 :
    print("Fortune 1")

elif fortune == 5 :
    print("Fortune 1")
