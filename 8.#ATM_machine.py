class ATM:
    def __init__(self):
        self.pin = ''
        self.balance = 0

        self.menu()

    def menu(self):
        user = input('''
              Hello, Choose from the following options:
            1. Press 1 to create pin
            2. Press 2 to deposit
            3. Press 3 to withdraw
            4. Press 4 to check balance
            5. Press 5 to exit\n''')
        
        if user == '1':
            self.create_pin()
           
        elif user == '2':
            self.deposti_amount()
                
        elif user == '3':
            self.withdraw_amount()
            
        elif user == '4':
            self.check_balance()
            
        else:
            print('Have a good day sir!')
            exit()

    def create_pin(self):
        print('Create Pin')
        self.pin = input("PIN: ")
        print('Pin creation successful!')


    def deposti_amount(self):
        deposit_pin = input('Enter PIN: ')
        if deposit_pin == self.pin:
            print("How much you want to deposit?")
            deposit = int(input("Enter amount: "))
            self.balance += deposit
        else:
            print('PIN Incorrect!')

    def withdraw_amount(self):
        withdraw_pin = input('Enter PIN: ')
        if withdraw_pin == self.pin:
            print("How much you want to withdraw?")
            withdraw = int(input('Enter amount: '))
            self.balance -= withdraw
        else:
            print('PIN Incorrect!')

    def check_balance(self):
        balance_pin = input("Enter PIN: ")
        if balance_pin == self.pin:
            print("Your current balance is: ", self.balance)
        else: 
            print('PIN Incorrect!')



atm = ATM()   
atm.deposti_amount()
atm.withdraw_amount()
atm.check_balance()

    