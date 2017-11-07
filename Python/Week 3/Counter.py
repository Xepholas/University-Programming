#Counter Program
import time
import random

Start = int(input("\nEnter the starting number: "))

End = int(input("\nEnter the ending number: "))

Count = int(input("\nEnter the rate of change: "))



for i in range(Start, End, Count) :
    print(i, end=" ")
