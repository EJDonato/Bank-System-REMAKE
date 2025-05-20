import mysql.connector
from mysql.connector.errors import IntegrityError
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="bank_system"
)

my_cursor = db.cursor()


def insert_account_info(gen_info, login_info):
    query_1 = '''
            INSERT INTO customer_list (first_name, last_name, birthdate, monthly_salary, account_number, bank_account_pin, balance)
            VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    query_2 = '''
            INSERT INTO user_login (account_number, email, password, user_type)
            VALUES (%s, %s, %s, %s)'''

    try:
        db.start_transaction()  # To execute simultaneously

        my_cursor.execute(query_1, gen_info)
        account_number = gen_info[4]
        login_params = (account_number, login_info[0], login_info[1], login_info[2])
        my_cursor.execute(query_2, login_params)

        db.commit()
        return "Success"  # Insertion successful. No Duplicates

    except IntegrityError as e:
        db.rollback()  # Rollback the transaction on error
        error_message = str(e)
        print(f"Error: {error_message}")

        if "Duplicate entry" in error_message:
            if "user_login.email" in error_message:
                return "Email DUPE"  # Email is the duplicate
            elif "user_login.account_number" in error_message:
                return "Account number DUPE"  # Account number is the duplicate
        else:
            raise  # Raise other errors if not IntegrityError


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

def verify_login_credentials(email, password, user_type):
    query = """
            SELECT  
                ul.account_number, 
                ul.email,
                ul.user_type,
                ul.status,
                cl.first_name,
                cl.last_name,
                cl.birthdate,
                cl.bank_account_pin,
                cl.monthly_salary,
                cl.balance
            FROM user_login ul
            LEFT JOIN customer_list cl ON ul.account_number = cl.account_number
            WHERE ul.email = %s AND ul.password = %s AND ul.user_type = %s
            """
    my_cursor.execute(query, (email, password, user_type))
    result = my_cursor.fetchone()

    if result is None:
        return None

    # Convert result to dictionary
    columns = [column[0] for column in my_cursor.description]
    result_dict = dict(zip(columns, result))
    # Convert some datas to processable data types
    result_dict["birthdate"] = str(result_dict["birthdate"])
    result_dict["monthly_salary"] = float(result_dict["monthly_salary"])
    result_dict["balance"] = float(result_dict["balance"]) 
    print(result_dict) 

    return result_dict  # returns user else none

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
