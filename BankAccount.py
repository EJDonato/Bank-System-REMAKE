class CreateBankAccount:
    def __init__(self,email,password,repassword,first_name,last_name, birthdate,monthly_salary,pin):
        self.email = email
        self.password = password
        self.repassword = repassword
        self.fullname = first_name + " " + last_name
        self.birthdate = birthdate
        self.monthly_salary = monthly_salary
        self.pin = pin

    def account_existing(self):
        email_existing = None #database inquiry dapat 'to and 'di ko sure if sa email ba talaga ichecheck if existing na
        if email_existing is not None:
            return False #send sa frontend

    def match_password(self):
        if self.password != self.repassword:
            return False #send sa frontend

    def check_pin(self):
        self.pin = str(self.pin)
        if len(self.pin) != 6: #'di ko rin sure if 6 digits ba pin natin
            return False #send sa frontend

    def insert_account_info(self):
        account_info = (self.email, self.password, self.fullname, self.birthdate, self.monthly_salary, self.pin)
        # sql inquiry para ma-insert 'to


# account = CreateBankAccount("airamjeanr@gmail.com","airamjean", "airamjean", "Airam", "Reglos","Mar1105", 20000, 1234567)






