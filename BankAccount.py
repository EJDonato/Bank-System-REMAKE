import random

class CreateBankAccount:
    def __init__(self,email,password,repassword,first_name,last_name, birthdate,pin, monthly_salary, initial_balance):
        self.email = email
        self.password = password
        self.repassword = repassword
        self.firstname = first_name
        self.lastname = last_name
        self.birthdate = birthdate #i want the format to be in MM-DD-YYYY
        self.monthly_salary = monthly_salary
        self.pin = pin
        self.initial_balance = initial_balance
        self.account_number = None
        self.status = "Pending"
        self.is_locked = False

    # to check if email is already existing
    def account_existing(self):
        email_existing = None
        if email_existing is not None:
            return False

    # to check if the entered password and re-entered password match
    def match_password(self):
        if self.password != self.repassword:
            return False

    #to check if pin is 6 digits
    def check_pin(self):
        self.pin = str(self.pin)
        if len(self.pin) != 6:
            return False

    #papalitan need id index hay
    def generate_account_number(self):
        self.birthdate_str = self.birthdate.replace("-", "")
        length = len(self.birthdate_str)
        self.account_number = "".join(random.sample(self.birthdate_str, k=length))
        while self.account_number in db: #para ma-check if may kaparehong accnum
            self.account_number = "".join(random.sample(self.birthdate_str, k=length))
        # # if wala yung na-generate na acc num sa db iistore

    # for db
    def insert_account_info(self):
        account_info = (self.firstname, self.lastname, self.birthdate, self.password, self.account_number, self.pin, self.monthly_salary, self.initial_balance, self.is_locked, self.status)
        # sql inquiry para ma-insert 'to tapos object daw pala hindi tuple so papalitan din toh,,, xd





