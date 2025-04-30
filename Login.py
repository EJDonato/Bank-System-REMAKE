class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

#will check kasi sabi ni amran siya na raw magchecheck???
    def check_account(self):
        email_db = "airamjeanr@gmail.com" #email from database
        password_db = "airamjean" #email from dsatabase
        status_db = "Pending"

        if email_db == self.email and password_db == self.password:
            if status_db == "Pending":
                return "Pending"
            else:
                return "Active"
        else:
            return "Not matched"

