import random
gussing_number=random.randint(1,100)
attempts=0
while 1:
    print('GUESS THE NUMBER BETWEEN 1 TO 100.')
    guess=int(input('Enter number you gussed :'))
    attempts +=1
    if guess==gussing_number:
        print('CONGRTULAIONS! YOU GUSSED THE CORRECT NUMBER..')
    elif guess<gussing_number:
        print('try HIGHER NUMBER.')
    else:
        print('try LOWER NUMBER.')
