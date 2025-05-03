class CreateBankAccount:
    def __init__(self,email,password,first_name,last_name, birthdate, pin, monthly_salary, initial_balance):
        self.email = email
        self.password = password
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
        email_not_existing = is_email_exist(self.email) #sql query
        if email_not_existing is False:
            return False #email is already existing
        else:
            return True #hindi pa nag-eexist email

    # generate a unique account number using bday and id index
    def generate_account_number(self):
        id_index = "1" #need sql query
        self.birthdate_str = self.birthdate.split("-")
        month = self.birthdate_str[0]
        day = self.birthdate_str[1]
        year = (self.birthdate_str[2])[-2:]
        self.account_number = year + id_index + day + month + id_index

    def insert_account_info(self):
        account_info = (self.firstname, self.lastname, self.birthdate, self.email,
                        self.password, self.account_number, self.pin, self.monthly_salary,
                        self.initial_balance, self.is_locked, self.status)
        insert_account_info(account_info) #sql query
        join_login_list() #sql query



# a = CreateBankAccount("airamjeanr@gmail.com", "airamjean", "Airam Jean", "Reglos",
#                       "03-11-2005", "123456", 50000, 10000)
# a.generate_account_number()
# a.insert_account_info()
