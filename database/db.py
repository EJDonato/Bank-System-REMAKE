import mysql.connector
from mysql.connector.errors import IntegrityError
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Htyc3v4d3v4d",
    database="bank_system"
)

my_cursor = db.cursor()


def insert_account_info(gen_info, login_info):
    query_1 = '''
            INSERT INTO customer_account_creation(first_name, last_name, birthdate, monthly_salary, account_number, bank_account_pin, balance)
            VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    query_2 = '''
            INSERT INTO user_login(account_number, email, password)
            VALUES (%s, %s, %s)'''

    try:
        db.start_transaction()  # To execute simultaneously

        my_cursor.execute(query_1, gen_info)
        account_number = gen_info[4]
        login_params = (account_number, login_info[0], login_info[1])
        my_cursor.execute(query_2, login_params)

        db.commit()
        return False  # Insertion successful. No Duplicates

    except IntegrityError as e:
        if e:
            return True   # Insertion unsuccessful. Duplicates exists
        else:
            raise  # Raise other error if not IntegrityError

def user_login():
    query = '''
    INSERT INTO user_login(account_number)
    SELECT cac.account_number
    FROM customer_account_creation cac 
        LEFT JOIN user_login ul ON cac.account_number = ul.account_number
    WHERE ul.account_number IS NULL;
    '''
    my_cursor.execute(query)
    db.commit()

def verify_login_credentials(email, password) -> bool:
    query = "SELECT status FROM user_login WHERE email = %s AND password = %s"
    my_cursor.execute(query, (email, password))
    result = my_cursor.fetchone()
    if result is not None:
        return result[0]    # if matched, return status
    else:
        return False


def customer_list():
    query = '''
    INSERT INTO customer_list(
        index_id,
        first_name,
        last_name,
        birthdate,
        monthly_salary,
        account_number,
        bank_account_pin,
        balance,
        loan_balance,
        is_locked)
    SELECT 
        cac.index_id, 
        cac.first_name, 
        cac.last_name, 
        cac.birthdate, 
        cac.monthly_salary, 
        ul.account_number, 
        cac.bank_account_pin, 
        cac.balance, 
        0 AS loan_balance, 
        FALSE AS is_locked
    FROM 
        customer_account_creation cac
    INNER JOIN user_login ul ON cac.email = ul.email
    LEFT JOIN customer_list cl ON cac.index_id = cl.index_id;
'''
    my_cursor.execute(query)
    db.commit()
