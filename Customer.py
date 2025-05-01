class Customer_Functions:
    def __init__(self):
        pass

    def authenticate(pin):
        checker = autheticate(pin)
        #sql query that will check if match yung pin sa db

        if checker is True:
            return True
        else:
            return False


    # TRANSACT WITH TELLER
    def transact_with_teller_withdraw(amount):
        balance_db = 10000  # balance from db

        if amount < balance_db:
            balance_db -= amount
            # sql query to add back balance sa db
            return True #withdraw successfully
        else:
            return False

    def transact_with_teller_deposit(amount):
        balance_db = 10000  # from db
        balance_db += amount
        # sql query to add back balance sa db
        return True #deposit successfully


    # USE ATM
    def use_atm_withdraw(amount):
        balance_db = 10000  #balance from db

        if amount <= 20000 and amount < balance_db:
            balance_db -= amount
            #sql query para palitan database
            return True #withdraw successfully
        else:
            return False

    def use_atm_deposit(amount):
        balance_db = 10000  # from db

        if amount <= 20000:
            balance_db += amount
            return True #deposit successfully
        else:
            return False

    def use_atm_change_pin(current_pin, new_pin):
        current_pin_db = 123456 #from db

        if current_pin == current_pin_db:
            #sql query to change pin sa db
            return True #pin successfully changed
        else:
            return False


    # REQUEST LOAN
    def pay_loan(amount):
        loan_db = 10000 #db
        loan_db -= amount

        if loan_db == 0:
            return True #pwede na mag-request
        else:
            return False

    def loan_request(amount):
        monthly_salary_db = 10000  # from database
        rate = monthly_salary_db * 0.400

        if amount <= rate:
            return True #pwede mag-request
        else:
            return False
