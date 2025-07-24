class bank:
    def __init__(self):
        self.balance=1000

    def credit(self):
        money=int(input("Enter the money for the credit:"))
        self.balance+=money
        print("Credit is :",self.balance)

class Banks(bank):
    def debit(self):
        money=int(input("Enter the money for the debit:"))
        self.balance-=money
        print("Debit is :",self.balance)

b =Banks()
b.credit()
b.debit()
