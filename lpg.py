"""Convert a volume in gallons to liters"""

#1. Setup
lpg= 3.785411784
#2. Input
print('How many gallons?')
gallons= float(input())
#3. Transform
liters= gallons * lpg
#4. Output
print(str(gallons) + ' gallons is equivelent to ' + str(liters) + ' liters')
