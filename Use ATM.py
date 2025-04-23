class useATM:
    def authenticate(self, pin):
        self.pin = pin
        pin_db = 123456 #pin from database

        if self.pin == pin_db:
            return True

    def withdraw(self, amount):
        self.amount = amount
        balance_db = 10000 #balance from database

        if self.amount <= 20000 and self.amount < balance_db:
            balance_db -= self.amount #tapos palitan database
            return True

    def deposit(self, amount):
        self.amount = amount
        balance_db = 10000 #from db

        if self.amount <= 20000:
            balance_db += self.amount
            return True

    def change_pin(self, current_pin, new_pin, ver_new_pin):
        self.current_pin = current_pin
        self.new_pin = new_pin
        self.ver_new_pin = ver_new_pin
        current_pin_db = 123456 #from db

        if self.current_pin == current_pin_db and self.new_pin == self.ver_new_pin:
            #change pin sa database
            return True

