class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_account(self):
        login = (self.email, self.password)
        login_result = verify_login_credentials(login)
        #either False, Pending, Active ang irereturm

        if login_result == "Active":
            return "Active"
        elif login_result == "Pending":
            return "Pending"
        else:
            return False
