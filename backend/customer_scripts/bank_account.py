

class BankAccount:
    def __init__(self, email, password, first_name, last_name, birthdate, pin, monthly_salary, initial_balance):
        self.email = email
        self.password = password
        self.firstname = first_name
        self.lastname = last_name
        self.birthdate = birthdate  # i want the format to be in MM-DD-YYYY
        self.pin = pin
        self.monthly_salary = monthly_salary
        self.initial_balance = initial_balance
        self.account_number = None
        