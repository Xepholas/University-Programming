#Word Guessing 1.0
import random

Words = ("python", "testing", "guessing", "programming", "answer")

word = random.choice(Words)

print("I've thought up a word and want you to guess it!")
print("\nAs a hint, I'll tell you that there are", len(word),"letters in the word!")
print("\nHow about I give you 5 chances to find some of the letters before you guess?")

L_1 = input("\nTake your first guess at a letter! ")

if L_1 in word :
    print("\nYes, that letter is in the word.")
else :
    print("\nNope, too bad.")

L_2 = input("\nTake your second guess at a letter! ")

if L_2 in word :
    print("\nYes, that letter is in the word.")
else :
    print("\nNope, too bad.")

L_3 = input("\nTake your third guess at a letter! ")

if L_3 in word :
    print("\nYes, that letter is in the word.")
else :
    print("\nNope, too bad.")

L_4 = input("\nTake your fourth guess at a letter! ")

if L_4 in word :
    print("\nYes, that letter is in the word.")
else :
    print("\nNope, too bad.")

L_5 = input("\nTake your fifth guess at a letter! ")

if L_5 in word :
    print("\nYes, that letter is in the word.")
else :
    print("\nNope, too bad.")

Guess = input("Okay, so what is the word? ")
if Guess == word :
    print("Congrats, you've won!")
else :
    print("Too bad, guess I win!")
