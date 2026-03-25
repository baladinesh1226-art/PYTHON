class bank():
    def __init__(self,name,accoutNumber):
        self.name = name
        self.accoutNumber = accoutNumber
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"available balance{self.balance}")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"available balance{self.balance}")

    def checkBalance(self):
        print(self.balance)


customer = bank('Dinesh',476069)
customer.deposit(10000)
customer.withdraw(100)
customer.checkBalance()
