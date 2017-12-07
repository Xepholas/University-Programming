#Character Creator 1.0c
import random, time, shelve, pickle

#Variables
menu=0
choice=0
Character=False
change=0
changeloop=0
delloop=0
delop=0
#Temp. Stats
STRT=1
DEFT=1
AGIT=1
LUKT=1
INTT=1
#Character Stats
STR=0
DEF=0
AGI=0
LUK=0
INT=0
AP=100
#Creator Variables
create=0
createchoice=0
Gender=("")
Class=("")
Name=("")
GenderT=("")
ClassT=("")
NameT=("")
exitcreate=("")
createxit=0
genloop=0
classloop=0
strloop=0
defloop=0
agiloop=0
lukloop=0
intloop=0
nameloop=0
strop=0
defop=0
agiop=0
lukop=0
intop=0
Nameop=0
Nameloop=0
APloop=0
APop=0
#Export Variables
STRE=("")
DEFE=("")
AGIE=("")
LUKE=("")
INTE=("")

#Functions
def export():
    """Exporting Function"""
    exports=open("export.dat", "wb")
    file=[Name, Gender, Class, STR, DEF, AGI, LUK, INT]
    print(file)
    pickle.dump(file, exports)
    exports.close()

def imports():
    """Importing Function"""
    imported=open("export.dat", "rb")
    data=pickle.load(imported)
    print(data)
    global Name
    global Gender
    global Class
    global STR
    global DEF
    global AGI
    global LUK
    global INT
    Name=data[0]
    Gender=data[1]
    Class=data[2]
    STR=data[3]
    DEF=data[4]
    AGI=data[5]
    LUK=data[6]
    INT=data[7]
    imported.close

#Start
print("Welcome to the character creation menu!")
print("Here, you can build a character of your choice by using attribute points.")

while menu==0:
    print("""
What would you like to do?
--------------------------
0 - New Character
1 - View Character
2 - Delete Character
3 - Export Character
4 - Import Character
5 - Quit
--------------------------
          """)

    choice=int(input("Pick an option: "))

    if choice==0:
        #CHARACTER CREATOR
        if Character==False:
            print("\n--------------------------------")
            print("Character Creation Menu")
            print("\nWelcome! In creating your character, you can choose the gender and class of yourcharacter and then assign them 100 attribute points into their stats. Each stat (STR, DEF,AGI, LUK and INT) are capped at 50 attribute points and start with a  base value of one.")
            print("--------------------------------")
            createchoice=0
            while createchoice==0:
                print("Name:", NameT)
                print("Gender:", GenderT)
                print("Class:", ClassT)
                print("--------------------------")
                print("Attribute Points:", AP)
                print("STR:", STRT)
                print("DEF:", DEFT)
                print("AGI:", AGIT)
                print("LUK:", LUKT)
                print("INT:", INTT)
                print("--------------------------")
                print("""
What would you like to do?
--------------------------
0 - Set Gender
1 - Set Class
2 - Alter STR
3 - Alter DEF
4 - Alter AGI
5 - Alter LUK
6 - Alter INT
7 - Name Character
8 - Finish Character
9 - Quit
--------------------------
                  """)

                create=int(input("Pick an option: "))

                if create==0:
                    #Gender Menu
                    genloop=0
                    while genloop==0:
                        print("\n--------------------------")
                        print("Current Gender:", GenderT)
                        GenderT=str(input("\nChoose a gender for your character: [M/F]"))
                        if GenderT.lower()=="m":
                            print("\nGender set to Male.")
                            print("--------------------------\n")
                            GenderT=("Male")
                            genloop=1

                        elif GenderT.lower()=="f":
                            print("\nGender set to Female.")
                            print("--------------------------\n")
                            GenderT=("Female")
                            genloop=1

                        else:
                            print("\nInvalid Input!")
                            GenderT=("")
                            
                elif create==1:
                    #Class Menu
                    classloop=0
                    while classloop==0:
                        print("\n--------------------------")
                        print("Current Class:", ClassT)
                        ClassT=str(input("\nChoose a class [Warrior, Mage, Thief]:"))
                        if ClassT.lower()=="warrior":
                            print("\nClass set to Warrior.")
                            print("--------------------------\n")
                            ClassT=("Warrior")
                            classloop=1

                        elif ClassT.lower()=="mage":
                            print("\nClass set to Mage.")
                            ("--------------------------\n")
                            ClassT=("Mage")
                            classloop=1
                            
                        elif ClassT.lower()=="thief":
                            print("\nClass set to Thief")
                            print("--------------------------\n")
                            ClassT=("Thief")
                            classloop=1
                            
                        else:
                            print("\nInvalid Input!")
                            print("\n--------------------------\n")
                            ClassT=("")
                            
                elif create==2:
                    #STR Set
                    strloop=0
                    while strloop==0:
                        print("\n--------------------------")
                        print("Current Attribute Points:", AP)
                        print("\nCurrent Strength Points:", STRT)
                        strop=str(input("\nWould you like to change this stat? [y/n]:"))
                        if strop.lower()=="y":
                            STRTT=STRT
                            changeloop=0
                            while changeloop==0:
                                STRTT=STRT
                                change=int(input("\nBy how many points would you like to change this stat? [-50 to 50]: "))
                                if change<-49:
                                    print("\nInvalid Value!")
                                    change=0
                                elif change>49:
                                    print("\nInvalid Value!")
                                    change=0
                                else:
                                    STRTT+=change
                                    if STRTT>50:
                                        print("\nError! Invalid Outcome!")
                                    elif STRTT<1:
                                        print("\nError! Invalid Outcome!")
                                    else:
                                        print("\nChanges committed.")
                                        print("\n--------------------------")
                                        STRT=STRTT
                                        AP-=change
                                        strloop=1
                                        changeloop=1
                                        
                            
                        elif strop.lower()=="n":
                            print("\n--------------------------\n")
                            strloop=1
                        else:
                            print("\nInvalid Input!")
                            print("\n--------------------------\n")
                            
                elif create==3:
                    #DEF Set
                    defloop=0
                    while defloop==0:
                        print("\n--------------------------")
                        print("Current Attribute Points:", AP)
                        print("\nCurrent Defence Points:", DEFT)
                        defop=str(input("\nWould you like to change this stat? [y/n]:"))
                        if defop.lower()=="y":
                            DEFTT=DEFT
                            changeloop=0
                            while changeloop==0:
                                DEFTT=DEFT
                                change=int(input("\nBy how many points would you like to change this stat? [-50 to 50]: "))
                                if change<-49:
                                    print("\nInvalid Value!")
                                    change=0
                                elif change>49:
                                    print("\nInvalid Value!")
                                    change=0
                                else:
                                    DEFTT+=change
                                    if DEFTT>50:
                                        print("\nError! Invalid Outcome!")
                                    elif DEFTT<1:
                                        print("\nError! Invalid Outcome!")
                                    else:
                                        print("\nChanges committed.")
                                        print("\n--------------------------\n")
                                        DEFT=DEFTT
                                        AP-=change
                                        defloop=1
                                        changeloop=1
                                        
                            
                        elif defop.lower()=="n":
                            print("\n--------------------------\n")
                            defloop=1
                        else:
                            print("\nInvalid Input!")
                            print("\n--------------------------\n")


                elif create==4:
                    #AGI Set
                    agiloop=0
                    while agiloop==0:
                        print("\n--------------------------")
                        print("Current Attribute Points:", AP)
                        print("\nCurrent Agility Points:", AGIT)
                        agiop=str(input("\nWould you like to change this stat? [y/n]:"))
                        if agiop.lower()=="y":
                            AGITT=AGIT
                            changeloop=0
                            while changeloop==0:
                                AGITT=AGIT
                                change=int(input("\nBy how many points would you like to change this stat? [-50 to 50]: "))
                                if change<-49:
                                    print("\nInvalid Value!")
                                    change=0
                                elif change>49:
                                    print("\nInvalid Value!")
                                    change=0
                                else:
                                    AGITT+=change
                                    if AGITT>50:
                                        print("\nError! Invalid Outcome!")
                                    elif AGITT<1:
                                        print("\nError! Invalid Outcome!")
                                    else:
                                        print("\nChanges committed.")
                                        print("\n--------------------------\n")
                                        AGIT=AGITT
                                        AP-=change
                                        agiloop=1
                                        changeloop=1
                                        
                            
                        elif agiop.lower()=="n":
                            print("\n--------------------------\n")
                            agiloop=1
                        else:
                            print("\nInvalid Input!")
                            print("\n--------------------------\n")

                elif create==5:
                    #LUK Set
                    lukloop=0
                    while lukloop==0:
                        print("\n--------------------------")
                        print("Current Attribute Points:", AP)
                        print("\nCurrent Luck Points:", LUKT)
                        lukop=str(input("\nWould you like to change this stat? [y/n]:"))
                        if lukop.lower()=="y":
                            LUKTT=LUKT
                            changeloop=0
                            while changeloop==0:
                                LUKTT=LUKT
                                change=int(input("\nBy how many points would you like to change this stat? [-50 to 50]: "))
                                if change<-49:
                                    print("\nInvalid Value!")
                                    change=0
                                elif change>49:
                                    print("\nInvalid Value!")
                                    change=0
                                else:
                                    LUKTT+=change
                                    if LUKTT>50:
                                        print("\nError! Invalid Outcome!")
                                    elif LUKTT<1:
                                        print("\nError! Invalid Outcome!")
                                    else:
                                        print("\nChanges committed.")
                                        print("\n--------------------------\n")
                                        LUKT=LUKTT
                                        AP-=change
                                        lukloop=1
                                        changeloop=1
                                        
                            
                        elif lukop.lower()=="n":
                            print("\n--------------------------\n")
                            lukloop=1
                        else:
                            print("\nInvalid Input!")
                            print("\n--------------------------\n")
                    
                elif create==6:
                    #INT Set
                    intloop=0
                    while intloop==0:
                        print("\n--------------------------")
                        print("Current Attribute Points:", AP)
                        print("\nCurrent Intelligence Points:", INTT)
                        intop=str(input("\nWould you like to change this stat? [y/n]:"))
                        if intop.lower()=="y":
                            INTTT=INTT
                            changeloop=0
                            while changeloop==0:
                                INTTT=INTT
                                change=int(input("\nBy how many points would you like to change this stat? [-50 to 50]: "))
                                if change<-49:
                                    print("\nInvalid Value!")
                                    change=0
                                elif change>49:
                                    print("\nInvalid Value!")
                                    change=0
                                else:
                                    INTTT+=change
                                    if INTTT>50:
                                        print("\nError! Invalid Outcome!")
                                    elif INTTT<1:
                                        print("\nError! Invalid Outcome!")
                                    else:
                                        print("\nChanges committed.")
                                        print("\n--------------------------\n")
                                        INTT=INTTT
                                        AP-=change
                                        intloop=1
                                        changeloop=1
                                        
                            
                        elif intop.lower()=="n":
                            intloop=1
                        else:
                            print("\nInvalid Input!")

                elif create==7:
                    #Name Menu
                    Nameloop=0
                    while Nameloop==0:
                        Nameop=str(input("\nWould you like to change the name of your character? [y/n]: "))
                        if Nameop.lower()=="y":
                            NameT=str(input("\nChoose a name for your character: "))
                            print("\nName committed.")
                            print("\n--------------------------\n")
                            Nameloop=1
                        elif Nameop.lower()=="n":
                            print("\n--------------------------\n")
                            Nameloop=1
                        else:
                            print("\nInvalid Input!")
                               


                elif create==8:
                    #Finish Up
                    APloop=0
                    while APloop==0:
                        if AP<0:
                            print("\nError! You cannot proceed with negative AP!")
                            print("\n--------------------------\n")
                            APloop=1
                        elif AP>0:
                            print("\nError! You cannot proceed with leftover AP!")
                            print("\n--------------------------\n")
                            APloop=1
                        else:
                            APop=0
                            while APop==0:
                                print("\n--------------------------\n")
                                confirmchar=str(input("\nAre you satisfied with this character an would like to save it? [y/n]: "))
                                if confirmchar.lower()=="y":
                                    print("\nCharacter saved! You can now view them from the VIEW option on the main menu.")
                                    print("\nExiting back to main menu...")
                                    print("\n--------------------------\n")
                                    STR=STRT
                                    DEF=DEFT
                                    AGI=AGIT
                                    LUK=LUKT
                                    INT=INTT
                                    Class=ClassT
                                    Name=NameT
                                    Gender=GenderT
                                    AP=100
                                    STRT=1
                                    DEFT=1
                                    AGIT=1
                                    LUKT=1
                                    INTT=1
                                    ClassT=("")
                                    NameT=("")
                                    GenderT=("")
                                    Character=True
                                    APloop=1
                                    APop=1
                                    createchoice=1
                                elif confirmchar.lower()=="n":
                                    print("\n--------------------------\n")
                                    APloop=1
                                    APop=1
                                else:
                                   print("\nInvalid Input!")
                            
                elif create==9:
                    #Quit
                    createexit=1
                    while createexit==1:
                        exitcreate=str(input("\nWould you like to exit back to the menu? [y/n]: "))
                        if exitcreate.lower()=="y":
                            print("\nExiting back to main menu...")
                            print("\n--------------------------\n")
                            STR=1
                            DEF=1
                            AGI=1
                            LUK=1
                            INT=1
                            Class=("")
                            Name=("")
                            Gender=("")
                            Character=False
                            createexit=0
                            createchoice=1
                        elif exitcreate.lower()=="n":
                            print("\n--------------------------\n")
                            createexit=0
                        else:
                            print("\nInvalid Input!")


                else:
                    #Option Check
                    print("Invalid value! Please try again!")

        elif Character==True:
            print("\nYou already have a character!")
            print("\nIn order to make another, you must delete the current one. !MAKE SURE TO EXPORT   IF YOU WISH TO SAVE THEM!")

        else:
            print("\nAN UNEXPECTED ERROR HAS OCCURRED!")
            
    elif choice==1:
        #CHARACTER VIEWER
        if Character==True:
            print("\n--------------------------------")
            print("Currently Saved Character:")
            print("--------------------------")
            print("Name:", Name)
            print("Gender:", Gender)
            print("Class:", Class)
            print("--------------------------")
            print("STR:", STR)
            print("DEF:", DEF)
            print("AGI:", AGI)
            print("LUK:", LUK)
            print("INT:", INT)
            print("\n--------------------------------")
        else:
            print("\n--------------------------------")
            print("\nYou don't have a character saved here!")
            print("\nTo create one select NEW CHARACTER on the main menu.")
            print("\n--------------------------------")

    elif choice==2:
        #CHARACTER DELETION
        delloop=0
        while delloop==0:
            print("\n--------------------------------\n")
            delop=str(input("DO YOU WISH TO DO DELETE SAVED DATA? (THIS CANNOT BE UNDONE!) [y/n]: "))
            if delop.lower()=="y":
                print("\nData Reset!")
                print("\n--------------------------\n")
                STR=1
                DEF=1
                AGI=1
                LUK=1
                INT=1
                Class=("")
                Name=("")
                Gender=("")
                Character=False
                delloop=1
            elif delop.lower()=="n":
                print("\n--------------------------\n")
                delloop=1
            else:
                print("\nInvalid Input!")


            

    elif choice==3:
        print("\n--------------------------------")
        print("\nEXPORT CURRENTLY UNDER CONSTRUCTION!")
        print("\nExport to file complete!")
        export()

    elif choice==4:
        print("\n--------------------------------")
        print("\nCURRENTLY UNDER CONSTRUCTION!")
        print("\nImport from file complete!")
        imports()
        Character=True
        
    elif choice==5:
        print("\n--------------------------------")
        print("Goodbye!")
        menu=1

    else:
        print("\n--------------------------------")
        print("Invalid value! Please try again!")
