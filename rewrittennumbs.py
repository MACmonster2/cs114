"""Convert base-10 numbers between 1-99 to written english"""
"""replace abriviations"""
#1. Setup
def pfn():
    #pfn = prompt for number
    """prompt user for a base-10 number and return it as an int."""
    print('Enter number between 1 and 99')
    return int(input())

def gtd(num):
    #gtd = get tens didgit
    """return the tens didgit of a number. number must be less than 100"""
    return num // 10

def god(num):
    #god = get ones didgit
    """return ones didgit of a number"""
    return num % 10
#2. Input
#print('Enter number between 1 and 99')
#num = int(input())
#3. Transform

#if num == 11:
#    output='eleven'
#elif num == 12:
#    output='twelve'
#elif num == 13:
#    output='thirteen'
#elif num == 15:
#    output='fifteen'
#elif num == 18:
#    output='eighteen'
#else:
#    tens = num // 10
#    ones = num % 10

def tdtw(gtd):
    #tdtw = tens didgit to word
    """change tens number to words"""
    if gtd == 9:
        tw='ninety'
    elif gtd == 8:
        tw='eighty'
    elif gtd == 7:
        tw='seventy'
    elif gtd == 6:
        tw='sixty'
    elif gtd == 5:
        tw='fifty'
    elif gtd == 4:
        tw='fourty'
    elif gtd == 3:
        tw='thirty'
    elif gtd == 2:
        tw='twenty'
    elif gtd == 1:
        tw='ten'
        #tw = tens word

def odtw(god):
    #odtw = ones didgit to word
    """change ones didgit to words"""
    if god == 9:
        ow='nine'
    elif god == 8:
        ow='eight'
    elif god == 7:
        ow='seven'
    elif god == 6:
        ow='six'
    elif god == 5:
        ow='five'
    elif god == 4:
        ow='four'
    elif god == 3:
        ow='three'
    elif god == 2:
        ow='two'
    elif god == 1:
        ow='one'
        #ow = ones word

def assemble_words():
    if gtd == 0:
        return odtw
    elif gtd == 1:
        return odtw,tdtw
    else:
       return tdtw + '-' + odtw

#4. Output
num=pfn()

tens=gtd(num)
ones=god(num)
tw=tdtw(tens)
ow=odtw(ones)
output=assemble_words(tens, ones, tdtw, odtw)

print(output)
