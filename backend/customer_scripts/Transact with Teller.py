def authenticate(pin):
    pin_db = 123456  #pin from database

    if pin == pin_db:
        return True

def withdraw(amount):
    balance_db = 10000  #balance from database

    if amount < balance_db:
        balance_db -= amount  #tapos palitan database
        return True

def deposit(amount):
    balance_db = 10000  #from db

    balance_db += amount
    return True

