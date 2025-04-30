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
    query = '''
    INSERT INTO customer_list(first_name, last_name, birthdate, email, password, account_number, bank_account_pin, monthly_salary, starting_balance, is_locked)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    my_cursor.execute(query, new_account)
    db.commit()

#
# new_account = ("Amran", "Gabarda", date(1989, 8, 8), "asdghg@gmail.com", "hakdog", "45877678", "437268", 6969.01, 100.03, True)
# insert_account_info(new_account)


def join_login_list():  # ILALAGAY YUNG EMAIL, PASSWORD SA TABLE CUSTOMER LOGIN SO AFTER MAGCREATE NG ACCOUNT NEED TO I RUN
    query = '''
    INSERT INTO customer_login (email, password)
    SELECT email, password 
    FROM customer_list'''
    my_cursor.execute(query)
    db.commit()

def verify_login_credentials(email, password):
    query = "SELECT * FROM customer_login WHERE email = %s AND password = %s"
    my_cursor.execute(query, (email, password))
    result = my_cursor.fetchone()   #kunin isa lang (yung nakuhang match)
    return result is not None

# # emailq = "amrangabarda2@gmail.com"
# # passwordq = "h4kdog"
# #
# # verify_login_credentials(emailq, passwordq)
#
def authenticate(bank_account_pin):
    query = "SELECT * FROM current_customer WHERE bank_account_pin = %s"
    my_cursor.execute(query, (bank_account_pin,))
    result = my_cursor.fetchone()
    return result is not None
#
def deposit(deposit_amount):
    query = "UPDATE current_customer SET starting_balance = %s"
    my_cursor.execute(query, (deposit_amount,))
    db.commit()

    return True

def update_customer_list_from_current():    # pang update from CURRENT CUSTOMER to CUSTOMER LIST kapag nag withdraw, deposit, change pin, or na lock
    query = '''
    UPDATE customer_list cl
    JOIN current_customer cc
    ON cl.account_number = cc.account_number
    SET cl.bank_account_pin = cc.bank_account_pin, cl.starting_balance = cc.starting_balance, cl.is_locked = cc.is_locked'''
    my_cursor.execute(query)
    db.commit()
