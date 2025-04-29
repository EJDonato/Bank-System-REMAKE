import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Htyc3v4d3v4d",
    database="practicedb"
)

my_cursor = db.cursor()

def insert_account_info(new_account):
    query = "INSERT INTO customer_login (first_name, last_name, birthdate, email, password, bank_account_pin, monthly_salary, starting_balance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    my_cursor.execute(query, new_account)
    db.commit()

# new_account = ("Amran", "Gabarda", date(1989, 8, 8), "amrangabarda2@gmail.com", "hakdog", "123456", 6969.01, 100.03)
#
# insert_account_info(new_account)


def verify_login_credentials(email, password):
    query = "SELECT * FROM customer_login WHERE email = %s AND password = %s"
    my_cursor.execute(query, (email, password))
    result = my_cursor.fetchone()   #kunin isa lang (yung nakuhang match)
    return result is not None

# emailq = "amrangabarda2@gmail.com"
# passwordq = "h4kdog"
#
# verify_login_credentials(emailq, passwordq)

def authenticate(bank_account_pin):
    query = "SELECT * FROM current_customer WHERE bank_account_pin = %s"
    my_cursor.execute(query, (bank_account_pin,))
    result = my_cursor.fetchone()
    return result is not None

def deposit(deposit_amount):
    query = "UPDATE current_customer SET starting_balance = %s"
    my_cursor.execute(query, (deposit_amount,))
    db.commit()

    return True