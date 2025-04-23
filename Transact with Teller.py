class TransactwithTeller:
    def authenticate(self, pin):
        self.pin = pin
        pin_db = 123456 #pin from database

        if self.pin == pin_db:
            return True

    def withdraw(self, amount):
        self.amount = amount
        balance_db = 10000  # balance from database

        if self.amount < balance_db:
            balance_db -= self.amount  # tapos palitan database
            return True

    def deposit(self, amount):
        self.amount = amount
        balance_db = 10000 #from db

        balance_db += self.amount
        return True