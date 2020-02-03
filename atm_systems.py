from accounts_info import *
from Transactions import *


def user_data():
    """contains user id and name"""
    data = {'0': 'Steve', '1': 'Michel'}
    return data


class Atm(Account):
    def __init__(self):
        super().__init__()

        # control flow for user selection
        pick = 0
        while pick != '4':
            self.menu()
            pick = self.get_option()
            if pick == '1':
                self.option_1()
            elif pick == '2':
                self.option_2()
            elif pick == '3':
                self.option_3()

    def menu(self):
        """menu screen"""
        print('''Main Menu \n1: Check Balance \n2: Withdraw \n3: Deposit \n4: Exit \n''')

    def get_option(self):
        """user screen options"""
        select = input('Enter selection: ')
        while select not in ['1', '2', '3', '4']:
            print('Invalid input. Please re-enter: ')
            select = input('Enter selection: ')
        return select

    def option_1(self):
        """option 1 functions"""
        print('Your current balance is ${:,.2f}\n'.format(self.get_balance()))

    def option_2(self):
        """option 2 functions"""
        try:
            amount = float(input('Enter withdraw amount: '))
        except ValueError:
            amount = float(input('Please re-enter the amount: '))
        withdraw(str(amount))
        self.withdraw(amount)
        print('\nWithdraw amount was ${:,.2f}'.format(amount))
        print('Your current balance is ${:,.2f}\n'.format(self.get_balance()))

    def option_3(self):
        """option 3 functions"""
        try:
            amount = int(input('Enter amount for deposit: '))
        except ValueError:
            amount = int(input('Please re-enter the amount: '))
        deposit(str(amount))
        self.deposit(amount)
        print('\nDeposit amount was ${:,.2f}'.format(amount))
        print('Your current balance is ${:,.2f}\n'.format(self.get_balance()))













