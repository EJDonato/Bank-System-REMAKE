import mysql.connector
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Htyc3v4d3v4d",
    database="practicedb"
)

my_cursor = db.cursor()

def insert_account_info(new_account):
    email = new_account[3]

    if is_email_exists(email):
        return False  # Returns False if email does exist.

    query = '''
            INSERT INTO customer_list(first_name, last_name, birthdate, email, password, account_number,
                                      bank_account_pin, monthly_salary, starting_balance, is_locked)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    my_cursor.execute(query, new_account)
    db.commit()

    return True  # Returns True if email does not exist yet.

def is_email_exists(email):
    query = '''
            SELECT COUNT(*)
            FROM customer_list
            WHERE email = %s
            '''
    my_cursor.execute(query, (email,))
    count = my_cursor.fetchone()[0]

    return count > 0

def join_login_list():  # ILALAGAY YUNG EMAIL, PASSWORD SA TABLE CUSTOMER LOGIN SO AFTER MAGCREATE NG ACCOUNT NEED TO I RUN
    query = '''
    INSERT INTO customer_login (email, password, status)
    SELECT email, password, status 
    FROM customer_list'''
    my_cursor.execute(query)
    db.commit()

def verify_login_credentials(email, password):
    query = "SELECT * FROM customer_login WHERE email = %s AND password = %s AND status = %s"
    my_cursor.execute(query, (email, password))
    result = my_cursor.fetchone()   #kunin isa lang (yung nakuhang match)
    return result is not None

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

def update_customer_list_from_current():    # pang update from CURRENT CUSTOMER to CUSTOMER LIST kapag nag withdraw, deposit, change pin, or na lock
    query = '''
    UPDATE customer_list cl
    JOIN current_customer cc
    ON cl.account_number = cc.account_number
    SET cl.bank_account_pin = cc.bank_account_pin, cl.starting_balance = cc.starting_balance, cl.is_locked = cc.is_locked'''
    my_cursor.execute(query)
    db.commit()
