#Car Sales Calculator
import time

print("Hello, this is the calculator to determine the total cost of a vehicle")
print("When prompted, please enter the base price of the vehicle")

time.sleep(1)

Vehicle = float(input("Base Cost of Vehicle:£"))

print("\nThank you, calculating total cost.")

def Load_slow(str):
    for letter in str:
        print(letter),
        time.sleep(1)

Load_slow("...")

print("Calculating License and Tax cost at 5% and 20% of original price.")

Load_slow("...")

print("Charging dealer preparation and destination fees of £150 and £80.")

Load_slow("...")

print("Calculation Complete!")
time.sleep(1)
Total = Vehicle + ((Vehicle/100)*20) + ((Vehicle/100)*5) + 230
print("\nTotal Cost: £", '%.2f' % Total)

Tot_01 = ((Vehicle/100)*20)
print("Tax Charged: £", '%.2f' % Tot_01)

Tot_02 = ((Vehicle/100)*5)
print("License Fee Charged: £", '%.2f' % Tot_02)

print("\n\n\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
input("Please press enter to exit")
