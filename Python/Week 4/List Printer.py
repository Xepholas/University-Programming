#List Printer
import random

List=["First", "Second", "Third", "Fourth", "Fifth"]

Loop = 5

while Loop > 0 :
    Index = int(len(List))
    Choice = random.randrange(Index)
    Word = List[Choice]
    print("\n", Word)
    List.remove(Word)
    Loop -= 1

