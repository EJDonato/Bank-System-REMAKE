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
            INSERT INTO user_login(account_number, email, password, user_type)
            VALUES (%s, %s, %s, %s)'''

    try:
        db.start_transaction()  # To execute simultaneously

        my_cursor.execute(query_1, gen_info)
        account_number = gen_info[4]
        login_params = (account_number, login_info[0], login_info[1], login_info[2])
        my_cursor.execute(query_2, login_params)

        db.commit()
        return False  # Insertion successful. No Duplicates

    except IntegrityError as e:
        error_message = str(e)

        if "Duplicate entry" in error_message:
            if "user_login.email" in error_message:
                return "Email DUPE"  # Email is the duplicate
            elif "user_login.account_number" in error_message:
                return "Account number DUPE"  # Account number is the duplicate
        else:
            raise  # Raise other errors if not IntegrityError

def verify_login_credentials(email, password):
    query = "SELECT account_number FROM user_login WHERE email = %s AND password = %s"
    my_cursor.execute(query, (email, password))
    result = my_cursor.fetchone()

    if result is not None:
        account_number = result[0]

        inner_query = '''
                SELECT
                    cl.first_name,
                    cl.last_name,
                    cl.birthdate,
                    cl.monthly_salary,
                    cl.account_number,
                    cl.bank_account_pin,
                    cl.balance,
                    cl.loan_balance,
                    ul.status
                FROM 
	                customer_list cl
                LEFT JOIN
	                user_login ul ON cl.account_number = ul.account_number
                WHERE cl.account_number = %s;'''

        my_cursor.execute(inner_query, (account_number,))
        inner_result = my_cursor.fetchone()
        return inner_result

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
