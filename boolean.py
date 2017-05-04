"""Convert base-10 numbers between 1-99 to written english"""

#1. Setup

#2. Input
print('Enter number between 1 and 99')
num = int(input())
#3. Transform
if num == 11:
    output='eleven'
elif num == 12:
    output='twelve'
elif num == 13:
    output='thirteen'
elif num == 15:
    output='fifteen'
elif num == 18:
    output='eighteen'
else:
    tens = num // 10
    ones = num % 10

    if tens == 9:
        tens_word='ninety'
    elif tens == 8:
        tens_word='eighty'
    elif tens == 7:
        tens_word='seventy'
    elif tens == 6:
        tens_word='sixty'
    elif tens == 5:
        tens_word='fifty'
    elif tens == 4:
        tens_word='fourty'
    elif tens == 3:
        tens_word='thirty'
    elif tens == 2:
        tens_word='twenty'
    elif tens == 1:
        tens_word='teen'

    if ones == 9:
        ones_word='nine'
    elif ones == 8:
        ones_word='eight'
    elif ones == 7:
        ones_word='seven'
    elif ones == 6:
        ones_word='sixty'
    elif ones == 5:
        ones_word='five'
    elif ones == 4:
        ones_word='four'
    elif ones == 3:
        ones_word='three'
    elif ones == 2:
        ones_word='two'
    elif ones == 1:
        ones_word='one'

    if tens == 0:
        output=ones_word
    elif tens == 1:
        output=ones_word+tens_word
    else:
        output=tens_word + '-' + ones_word

#4. Output
print(output)
