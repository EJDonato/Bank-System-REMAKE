
from datetime import datetime
import random

from database import insert_account_info


class Signup:
    ACC_NUM_DUPE = "Account number DUPE"
    EMAIL_DUPE = "Email DUPE"

    # Attempts to insert account info; regenerates account number if duplicate, returns False if email exists
    def insert_acc_info_to_database(self, bank_account, user_type):
        bank_account.account_number = self.generate_account_number()

        check = self.insert_query(bank_account, user_type)
        while check == self.ACC_NUM_DUPE:
            bank_account.account_number = self.generate_account_number()
            check = self.insert_query(bank_account, user_type)

        if check == self.EMAIL_DUPE:
            return False  # EMAIL IS ALREADY EXISTING
        else:
            return True  #SIGNUP SUCCESSFUL
        
    def generate_account_number(self):
        year = (str(datetime.today().date()))[2:4]
        digits = str(random.randint(100000, 999999))
        return year + digits
    
    def insert_query(self, bank_account, user_type):
        account_info = (bank_account.firstname, bank_account.lastname, bank_account.birthdate, bank_account.monthly_salary,
                        bank_account.account_number, bank_account.pin, bank_account.initial_balance)
        login_info = (bank_account.email, bank_account.password, user_type)

        ## SQL QUERY ##
        check = insert_account_info(account_info, login_info)

        return check

