print('Are you a vampire')
vampire = input()
vampup = vampire.upper()
if vampup == "NO":
    print('Of course not! Everyone knows vampires aren not real.')
else:
    print('How old are you?')
    age = int(input())
    if age <= 200:
        print('You are still very young. You must gain more knowlege.')
    elif age < 2000:
        print('You have much maturity and knowlege, but you require more. Come back when you have seen 2000 summers.')
    elif age >= 2000:
        print('Welcome to the family! We have been waiting for you.')
