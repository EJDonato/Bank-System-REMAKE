from database import verify_login_credentials


class Login:
    def check_account(self, email, password, user_type):
        ## SQL QUERY ##
        check = verify_login_credentials(email, password, user_type)

        return check

    