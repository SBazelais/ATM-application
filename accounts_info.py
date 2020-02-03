from Transactions import *

class Account:
    def __init__(self, id=0, balance = 1000):
        self._id = id
        self._balance = balance

    def get_id(self):
        """get ID"""
        return self._id

    def set_id(self, id):
        """setting ID"""
        self._id = id

    def set_balance(self, balance):
        """get balance"""
        new_balance = balance - withdraw_net() + deposit_net()
        self._balance = new_balance

    def get_balance(self):
        """setting balance"""
        return self._balance

    def withdraw(self, amount):
        """withdraw"""
        self._balance -= float(amount)

    def deposit(self, amount):
        """deposit"""
        self._balance += float(amount)






