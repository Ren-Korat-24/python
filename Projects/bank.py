class Bank:
    def __init__(self):
        self.name = ""
        self.acnum = 0
        self.password = ""
        self.balance = 0

    def personDetails(self):
        self.name = input("Enter the name: ")

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

    def creditMoney(self):
        money = int(input("Enter the Amount to deposit: "))
        self.balance += money
        print("Credit Successful.\nUpdated balance:", self.balance)

    def withdrawMoney(self):
        money = int(input("Enter the Amount to withdraw: "))
        if money > self.balance:
            print("Insufficient Balance...")
        else:
            self.balance -= money
            print("Withdrawal Successful.\nRemaining Balance:", self.balance)


# Main Program
AcountDetails = []

def account_exists(acnum):
    for a in AcountDetails:
        if a.acnum == acnum:
            return True
    return False

while True:
    print("\n========== Bank Management System ==========")
    print("\n1: Open Account")
    print("2: Show Accounts")
    print("3: Credit")
    print("4: Withdrawal")
    print("5: Exit")
    print("==========================================")
    choice = int(input("Choice: "))

    match choice:
        case 1:
            n = int(input("Number of new accounts to open: "))
            for _ in range(n):
                while True:
                    acnum = int(input("Enter a unique account number: "))
                    if account_exists(acnum):
                        print("Account already exists! Try another number.")
                    else:
                        break
                b = Bank()
                b.acnum = acnum  # Set unique account number
                b.personDetails()
                AcountDetails.append(b)
                print("Account created successfully.")

        case 2:
            print("\nName\tAccount no\tBalance")
            for a in AcountDetails:
                a.dis()

        case 3:
            fnum = int(input("Enter account number: "))
            account = None
            for a in AcountDetails:
                if a.acnum == fnum:
                    account = a
                    break
            if account:
                repass = input("Enter password: ")
                if account.password == repass:
                    account.creditMoney()
                else:
                    print("Incorrect password.")
            else:
                print("Account not found.Go to the case 1....")

        case 4:
            fnum = int(input("Enter account number: "))
            account = None
            for a in AcountDetails:
                if a.acnum == fnum:
                    account = a
                    break
            if account:
                repass = input("Enter password: ")
                if account.password == repass:
                    account.withdrawMoney()
                else:
                    print("Incorrect password.")
            else:
                print("Account not found.Go to the case 1....")

        case 5:
            print("Thank you for using the Bank System. Goodbye!")
            break

        case _:
            print("Invalid choice. Please try again.")
