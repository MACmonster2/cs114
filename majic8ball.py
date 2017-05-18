import random
from time import sleep
print('Ask me any qustion you wish, i will do my best to answer.')
input()
sleep(1)
def answer(answer_number):
    if answer_number == 1:
           return 'I am positive'
    elif answer_number == 2:
           return 'I have no answer for you'
    elif answer_number == 3:
           return 'Yes'
    elif answer_number == 4:
           return 'Reply is unclear try again'
    elif answer_number == 5:
           return 'Ask again later'
    elif answer_number == 6:
           return 'There is a good chance'
    elif answer_number == 7:
           return 'I think not'
    elif answer_number == 8:
           return 'Never'
    elif answer_number == 9:
           return 'Probably not'

r = random.randint(1, 9)
fortune = answer(r)
print(fortune)
