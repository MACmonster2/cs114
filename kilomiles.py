"""Convert miles and kilometers"""

#1. Setup
kpm = 1.60934
#2. Input
print('do you need miles or kilometers?')
d= (input())
if d in [miles, Miles]:
    print('How many miles to convert?')
    miles= float(input())
    #3. Transform
    kilometers= miles * kpm
    #4. Output
    print(str(miles) + ' miles is equivelent to ' + str(kilometers) + ' kilometers')
else:
    print('How many kilometers to convert?')
    kilometers= float(input())
    #3. Transform
    miles= kilometers / kpm
    #4. Output
    print(str(kilometers) + ' kilometers is equivelent to ' + str(miles) + ' miles')
