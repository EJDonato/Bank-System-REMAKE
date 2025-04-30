def authenticate(pin):
    pin_db = 123456  #pin from database

    if pin == pin_db:
        return True


def withdraw(amount):
    balance_db = 10000  #balance from database

    if amount <= 20000 and amount < balance_db:
        balance_db -= amount  #tapos palitan database
        return True


def deposit(amount):
    balance_db = 10000  #from db

    if amount <= 20000:
        balance_db += amount
        return True


def change_pin(current_pin, new_pin, ver_new_pin):
    current_pin_db = 123456  #from db

    if current_pin == current_pin_db and new_pin == ver_new_pin:
        #change pin sa database
        return True
