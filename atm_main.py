from atm_systems import *
from datetime import date

while True:
    # user input
    print('Welcome to XCapital')
    id = input('Please enter your id: ')

    # first control flow for id
    while id not in user_data():
        print('Invalid ID. Please re-enter: ')
        try:
            id = input('Enter id: ')
        except ValueError:
            id = input('invalid input please re-enter id: ')

    # second control flow to confirm id
    if id in user_data().keys():
        print('\nToday is {}'.format(date.today().strftime("%B %d, %Y")))
        print('Welcome {}!!!!\n'.format(user_data()[id]))

    # instantiation
    system = Atm()

    # invoking method
    system.menu()

