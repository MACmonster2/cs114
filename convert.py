"""Convert miles to kilometers"""

#1. Setup
kpm = 1.60934
#2. Input
print('How many miles to convert?')
miles= float(input())
#3. Transform
kilometers= miles * kpm
#4. Output
print(str(miles) + ' miles is equivelent to ' + str(kilometers) + ' kilometers')
