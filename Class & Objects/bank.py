class Bank:
    def __init__(self):
        self.name = ""
        self.acnum = 0
        self.password = ""
        self.balance = 0

    def personDetails(self):
        self.name = input("Enter the name: ")
        self.acnum = int(input("Enter the account number: "))

        while True:
            self.password = input("Enter the Password (min 8 characters): ")
            if len(self.password) >= 8:
                break
            else:
                print("Password is too short...")

        while True:
            self.balance = int(input("Enter Amount (minimum 2000): "))
            if self.balance >= 2000:
                break
            else:
                print("Minimum deposit is 2000!")


    def dis(self):
        print(f"{self.name}\t{self.acnum}\t\t{self.balance}")

    def creditMoney(self, repassword,acnum):
        if self.acnum==fnum:
            self.password == repassword
            money = int(input("Enter the Amount to deposit: "))
            self.balance += money
            print("Credit Successful.\nUpdated balance:", self.balance)
        else:
            print("Password Incorrect!")

    def withdrawMoney(self, repassword):
        if self.password == repassword:
            money = int(input("Enter the Amount to withdraw: "))
            if money > self.balance:
                print("Insufficient Balance...")
            else:
                self.balance -= money
                print("Withdrawal Successful.\nRemaining Balance:", self.balance)
        else:
            print("Password Incorrect!")



# Main Program
AcountDetails = []

while True:
    print("\n1: Open Account")
    print("2: Show Accounts")
    print("3: Credit")
    print("4: Withdrawal")
    print("5: Exit")
    choice = int(input("Choice: "))

    match choice:
        case 1:
            n = int(input("Number of new accounts to open: "))
            for _ in range(n):
                b = Bank()
                b.personDetails()
                AcountDetails.append(b)

        case 2:
            print("\nName\tAccount no\tBalance")
            for a in AcountDetails:
                a.dis()

        case 3:
            fnum = int(input("Enter account number: "))
            repass = input("Enter password: ")
            found = False
            for a in AcountDetails:
                   if a.creditMoney(repass):
                    found = True
                    break
            if not found:
                print("No account found.")

        case 4:
            fnum = int(input("Enter account number: "))
            repass = input("Enter password: ")
            found = False
            for a in AcountDetails:
                if a.withdrawMoney(repass):
                    found = True
                    break
            if not found:
                print("No account found.")

        case 5:
            print("Thank you for using the Bank System.")
            break

        case _:
            print("Invalid choice. Please try again.")
