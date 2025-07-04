"""
File: savingsaccount.py
This module defines the SavingsAccount class.
"""

class SavingsAccount:
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE = 0.02    # Single rate for all accounts

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string representation of the account."""
        return (f'Name:    {self.name}\n'
                f'PIN:     {self.pin}\n'
                f'Balance: {self.balance}')

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current pin."""
        return self.pin

    def deposit(self, amount):
        """If the amount is valid, adds it
        to the balance and returns None;
        otherwise, returns an error message."""
        if amount < 0:
            return "Error: Deposit amount must be positive"
        self.balance += amount

    def withdraw(self, amount):
        """Withdraws amount from account and returns status message."""
        if amount < 0:
            return "Error: Withdrawal amount must be positive"
        elif self.balance < amount:
            return "Error: Insufficient funds"
        else:
            self.balance -= amount

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

