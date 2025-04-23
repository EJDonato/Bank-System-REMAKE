class RequestLoan:
    def authenticate(self, pin):
        self.pin = pin
        pin_db = 123456 #pin from database

        if self.pin == pin_db:
            return True

    def pay_loan(self, amount):
        self.amount = amount
        loan_db = 10000 #db

        loan_db -= self.amount

        if loan_db == 0:
            return True #pwede na mag-request

    def loan_request(self, amount):
        self.amount = amount
        monthly_salary_db = 10000 #from database
        rate = monthly_salary_db * 0.400

        if self.amount <= rate:
            return True