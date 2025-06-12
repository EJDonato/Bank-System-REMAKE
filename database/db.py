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
            INSERT INTO customer_list (first_name, last_name, birthdate, monthly_salary, account_number, bank_account_pin, balance)
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


def verify_login_credentials(email, password, user_type):
    query = """
            SELECT  
                ul.account_number, 
                email,
                user_type,
                status,
                first_name,
                last_name,
                birthdate,
                bank_account_pin,
                monthly_salary,
                balance
            FROM user_login ul
            INNER JOIN customer_list cl 
                USING(account_number)
            WHERE ul.email = %s 
                AND ul.password = %s 
                AND ul.user_type = %s
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

def authenticate(account_number, pin): # receives pin and account number and authenticates if pin matches pin connected to account number
    query = '''
        SELECT * 
        FROM customer_list 
        WHERE account_number = %s 
            AND bank_account_pin = %s'''
    my_cursor.execute(query, (account_number, pin))
    result = my_cursor.fetchone()
    if result is None:
        return False
    
    return True

def update_balance(new_balance, account_number):
    query = '''
        UPDATE customer_list 
        SET balance = %s 
        WHERE account_number = %s'''
    my_cursor.execute(query, (new_balance, account_number))
    db.commit()
    