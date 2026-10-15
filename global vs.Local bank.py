bank_balance = 5000
def deposit(amount):
    global bank_balance
    bank_balance += amount
    print("Updated balance:", bank_balance)
    
def withdraw(amount):
    global bank_balance
    
    if amount <= bank_balance:
        bank_balance -= amount
        print("Updated balance:", bank_balance)
        
    else:
        print("insufficient balance!")
        
    deposit(1000)
    withdraw(2000)