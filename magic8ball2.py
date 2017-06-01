import random

seed_num=input('What would you like to know? ')

happy = len(seed_num) <=30

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'I am positive',
    'Possibly',
    'Reply hazy try again',
    'Reply is unclear try again',
    'Concentrate and ask again',
    'Your chances are not that great', #8
    'There is a good chance',
    'I doubt it',
    'I have no answer for you',
    'Ask again later',
    'Ask again later',
    'Very doubtful',
    'I think not',
    'Never',
    'Probably not']

if happy:
    result = messages[0:9]
else:
    result = messages[9:18]

print(result[random.randint(0, len(result) - 1)])
