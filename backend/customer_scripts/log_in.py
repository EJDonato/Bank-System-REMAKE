from database.db import verify_login_credentials


class Login:
    def check_account(self, email, password):
        ## SQL QUERY ##
        check = verify_login_credentials(email, password)

        if check is False:
            return False  # EMAIL AND PASSWORD MISMATCHED
        else:
            return(check)  # THIS WILL ONLY RETURN ACCOUNT NUMBER, EMAIL, PASSWORD, AND ROLE
                            # since the check is only used in user_login table