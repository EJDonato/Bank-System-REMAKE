import mysql.connector
from mysql.connector.errors import IntegrityError
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Htyc3v4d3v4d",
    database="practicedb"
)

my_cursor = db.cursor()

def insert_account_info(new_account):
        query = '''
                INSERT INTO customer_list(first_name, last_name, birthdate, email, password, account_number,
                                          account_pin, monthly_salary, starting_balance, is_locked, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        try:
            my_cursor.execute(query, new_account)
            db.commit()
            return False # Insertion successful. No Duplicates

        except IntegrityError as e:
            if e:
                return True # Insertion unsuccessful. Duplicates exists
            else:
                raise   # Raise other error if not IntegrityError

        finally:
            my_cursor.close()

'''
new_account = ['Amran', 'Gabarda', date(2005, 8,8), 'myemail@gmail.com', 'mypassword', 12345678, 123456, 50.00, 10.00, False, 'Active']
insert_account_info(new_account)
'''

def join_login_list():  # This should be run every successful execution of insert_account_info
    query = '''
    INSERT INTO customer_login (email, password, status)
    SELECT email, password, status 
    FROM customer_list'''
    my_cursor.execute(query)
    db.commit()

def verify_login_credentials(email, password, status) -> bool:  # if this executes True, current_customer() must be called.
    query = "SELECT * FROM customer_login WHERE email = %s AND password = %s AND status = %s"
    my_cursor.execute(query, (email, password, status))
    result = my_cursor.fetchone()
    return result is not None

'''
email = "myemail@mail.com"
password = "mypassword"
status = "Active"
print(verify_login_credentials(email, password, status))
'''

def current_customer():
    pass

def update_customer_list_from_current():    # pang update from CURRENT CUSTOMER to CUSTOMER LIST kapag nag withdraw, deposit, change pin, or na lock
    query = '''
    UPDATE customer_list cl
    JOIN current_customer cc
    ON cl.account_number = cc.account_number
    SET cl.bank_account_pin = cc.bank_account_pin, cl.starting_balance = cc.starting_balance, cl.is_locked = cc.is_locked'''
    my_cursor.execute(query)
    db.commit()

def authenticate(bank_account_pin):
    query = "SELECT * FROM current_customer WHERE bank_account_pin = %s"
    my_cursor.execute(query, (bank_account_pin,))
    result = my_cursor.fetchone()
    return result is not None
#
def get_current_balance():
    query = "SELECT starting_balance FROM current_customer"
    my_cursor.execute(query)
    return my_cursor.fetchone()[0]

def update_balance(new_balance):
    query = "UPDATE current_customer SET starting_balance = %s"
    my_cursor.execute(query, (new_balance,))
    db.commit()
