"""Change Calculator"""

#1. Setup
D= 1
q= .25
d= .1
n= .05
p= .01
#2. Input
print('How much change would you like back?')
change= float(input())
#print(change)
#3. Transform
dollars= change//D
#print(dollars)
change= change-dollars*D
#print(change)
quarters= change//q
#print(quarters)
change= change-quarters*q
#print(change)
dimes= change//d
#print(dimes)
change= change-dimes*d
#print(change)
nickles= change//n
#print(nickles)
change= round(change-nickles*n, 2)
#print(change)
pennies= change//p
#print(pennies)
#4. Output
print('You will recieve',int(dollars),'dollars,',int(quarters),'quarters,',int(nickles),'nickles,',
    int(dimes),'dimes, and',int(pennies),'pennies.')
