class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_account(self):
        email_db = "airamjeanr@gmail.com" #email from database
        password_db = "airamjean" #email from dsatabase

        if email_db == self.email and password_db == self.password:
            return True

