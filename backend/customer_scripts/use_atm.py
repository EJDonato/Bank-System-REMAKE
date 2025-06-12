import database

class UseATM:
    def validate_pin(self, pin, acc_number):
        correct_pin = str(database.fetch_pin(acc_number))
        print(f"Comparing {repr(correct_pin)} to input: {repr(pin)}")
        return True if pin == correct_pin else False
