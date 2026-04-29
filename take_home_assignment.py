class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount < 0 or type(float(amount)) != float: 
            print('the amount deposited must be a positive decimal number')
        else:
            self.balance += amount 
            print(f'your new balance is {self.balance}')

    def withdraw(self, amount: float):
        if amount < 0 or type(float(amount) != float): 
            print('the amount withdrawn must be a positive decimal number ')
        elif (self.balance - amount) < 0:
            print(f'your balance is 0 and you cannot withdraw anymore')
        else:
            self.balance = self.balance - amount
            print(f'your new balance is {self.balance}')


    def get_balance(self):
        return self.balance

    def str_(self):
        return f'Account Holder: {self.account_holder} Balance: {self.balance}'

class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance):
        super().__init__(account_holder,balance)

    def apply_interest(self):
        if self.balance < 1000:
            interest = self.balance * 0.03
            self.balance = self.balance + interest

        elif self.balance > 1001 and self.balance < 5000:
            interest = self.balance * 0.05
            self.balance = self.balance + interest 
        else:
            interest = self.balance * 0.07
            self.balance = self.balance + interest
    
    def str (self):
        return f'Account Holder: {self.account_holder} Balance: {self.balance}'

class CheckingAccount(BankAccount):
    def __init__(self,account_holder,balance):
        super().__init__(account_holder,balance)

    def withdraw(self, amount: float):
        if amount < 0 or type(float(amount) != float): 
            print('the amount withdrawn must be a positive decimal number ')
        elif (self.balance - amount) < -500:
            print('overdraft limit exceeded')
        elif (self.balance - amount) < 0:
            self.balance = self.balance - (amount + 25.0) 
            print(f'your new balance is {self.balance} which includes an overdraft fee of $25')
        else:
            self.balance = self.balance - amount
            print(f'your new balance is {self.balance}')


if __name__ == "__main__":
    import unittest 
    class TestAccounts(unittest.TestCase):
        def test_savings_account_deposit(self):
            savings = SavingsAccount("John Doe", 500)
            savings.deposit(200) # Deposit $200
            self.assertEqual(savings.get_balance(), 700) # New balance should be 700
        def test_savings_account_interest_below_1000(self):
            savings = SavingsAccount("John Doe", 800)
            savings.apply_interest() # Interest at 3% for balance less than 1000
            self.assertAlmostEqual(savings.get_balance(), 824, places=2) # 800 + 3% of 800 = 824
        def test_savings_account_interest_between_1001_and_5000(self):
            savings = SavingsAccount("Jane Smith", 1500)
            savings.apply_interest() # Interest at 5% for balance between 1001 and 5000
            self.assertAlmostEqual(savings.get_balance(), 1575, places=2) # 1500 + 5% of 1500 = 1575
        def test_checking_account_overdraft(self):
            checking = CheckingAccount("Alex Lee", 200)
            checking.withdraw(300) # Withdraw $300, which goes negative
            self.assertEqual(checking.get_balance(), -125) # Balance should be -125 after overdraft and fee
    unittest.main()