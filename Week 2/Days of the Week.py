#Day of the week program
import time
hldy = False

while hldy == False :
    Day = str(input("\nPlease enter a day of the week! "))
    
    if Day.lower() == "monday" :
        print("\nMonday!")

    elif Day.lower() == "tuesday" :
        print("\nTuesday!")
        
    elif Day.lower() == "wednesday" :
        print("\nWednesday!")
        
    elif Day.lower() == "thursday" :
        print("\nThursday!")
        
    elif Day.lower() == "friday" :
        print("\nFriday!")
        
    elif Day.lower() == "saturday" :
        print("\nSaturday!")
        
    elif Day.lower() == "sunday" :
        print("\nSunday!")

    elif Day.lower() == "holiday":
        print("\nWha? It's a holdiday?! Bye!")
        hldy = True
        
    else :
        print("\nInvalid Input! Please Try Again!")
        



