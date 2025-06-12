import database

class Login:
    def check_account(self, email, password, user_type):
        ## SQL QUERY ##
        check = database.verify_login_credentials(email, password, user_type)

        return check
    
    def fetch_data(self, acc_num):
        data = database.fetch_data(acc_num)
        return data

    