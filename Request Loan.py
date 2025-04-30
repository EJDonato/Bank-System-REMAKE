def authenticate(pin):
    pin_db = 123456  #pin from database

    if pin == pin_db:
        return True

def pay_loan(amount):
    loan_db = 10000 #db
    loan_db -= amount

    if loan_db == 0:
        return True #pwede na mag-request

def loan_request(amount):
    monthly_salary_db = 10000 #from database
    rate = monthly_salary_db * 0.400

    if amount <= rate:
        return True