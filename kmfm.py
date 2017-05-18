"""Convert miles and kilometers"""

#1. Setup
kpmi = 1.60934
fpm = 3.28084

#2. Input
print('Do you want to convert feet, meters, miles, or kilometers')
measure= (input())
d= measure.lower()
if d == ('miles'):
    print('How many miles to convert?')
    miles= float(input())
    #3. Transform
    kilometers= miles * kpmi
    #4. Output
    print(str(miles) + ' miles is equivelent to ' + str(kilometers) + ' kilometers')
elif d== ('feet'):
    print('How many feet to convert?')
    feet= float(input())
    #3. Transform
    meters= feet / fpm
    #4. Output
    print(str(feet) + ' feet is equivelent to ' + str(meters) + ' meters')
elif d== ('meters'):
    print('How many meters to convert?')
    meters= float(input())
    #3. Transform
    feet= meters * fpm
    #4. Output
    print(str(meters) + ' meters is equivelent to ' + str(feet) + ' feet')
else:
    print('How many kilometers to convert?')
    kilometers= float(input())
    #3. Transform
    miles= kilometers / kpmi
    #4. Output
    print(str(kilometers) + ' kilometers is equivelent to ' + str(miles) + ' miles')
