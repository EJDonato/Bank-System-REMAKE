from .sign_up import Signup
from .log_in import Login
from .bank_account import BankAccount

class CustomerFacade:
    def __init__(self):
        self.bank_account = None

        self.signup = Signup()
        self.login = Login()

    def sign_up(self, email, password, first_name, last_name, birthdate, pin, monthly_salary, initial_balance, user_type):
        self.bank_account = BankAccount(email, password, first_name, last_name, birthdate, pin, monthly_salary, initial_balance)
        success = self.signup.insert_acc_info_to_database(self.bank_account, user_type)

        print("Inserting account info to database...")
        
        if success:
            print("Account info inserted successfully. Signup complete.")
            return True
        else:
            print("Account info insertion failed. Signup unsuccessful.")   
            return False

    def log_in(self, email, password, user_type):
        get_user_info = self.login.check_account(email, password, user_type)
        return get_user_info  # returns user else none
