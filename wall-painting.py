"""Wall to paint ratio"""
from time import sleep
#1. Setup
gpsf= 400
#2. Input
print('How wide is the wall?')
width= float(input())
sleep(1)
print('What is the height of the wall?')
height= float(input())
sleep(1)
print('How much does a gallon of paint cost?')
price= float(input())
print('How many coats do you want?')
coats= float(input())
#3. Transform
sqft= width*height
layer= sqft/gpsf
cost= coats*price*layer
#4. Output
print('It would cost',cost,'dollars to paint the wall once')
