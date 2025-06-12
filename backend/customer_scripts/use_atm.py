import database

class UseATM:
    def validate_pin(self, pin, acc_number):
        correct_pin = str(database.fetch_pin(acc_number))
        print(f"Comparing {repr(correct_pin)} to input: {repr(pin)}")
        return True if pin == correct_pin else False
    
    def update_balance(self, new_bal, acc_num):
        result = database.update_balance(new_bal, acc_num)
        return result