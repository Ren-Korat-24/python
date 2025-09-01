
class Bank:
    #Constructor
    def __init__(self):
        self.name = ""
        self.acnum = 0
        self.password = ""
        self.balance = 0

    #Basic Details
    def personDetails(self):
        self.name = input("Enter the name: ")
        # check Passoword
        while True:
            self.password = input("Enter the Password (min 8 characters): ")
            if len(self.password) >= 8:
                break
            else:
                print("Password is too short...")
    #Check Balance
        while True:
            self.balance = int(input("Enter Amount (minimum 2000): "))
            if self.balance >= 2000:
                break
            else:
                print("Minimum deposit is 2000!")

    #Display
    def displayDetails(self):
        print(f"{self.name}\t{self.acnum}\t\t{self.balance}")

    #Credit
    def creditMoney(self):
        money = int(input("Enter the Amount to deposit: "))
        self.balance += money
        print("Credit Successful.Updated balance:", self.balance)

    #Debit
    def withdrawMoney(self):
        money = int(input("Enter the Amount to withdraw: "))
        if money > self.balance:
            print("Insufficient Balance...")
        else:
            self.balance -= money
            print("Withdrawal Successful...\nRemaining Balance:", self.balance)

    #Tranfer
    def transferMoney(self, amount, receiver):
        if amount > self.balance:
            print("Insufficient Balance.Transfer Failde..")
        else:
            self.balance -= amount
            receiver.balance += amount
            print(f"₹{amount} transferred successfully to Account {receiver.acnum}")
            print(f"Your remaining balance: ₹{self.balance}")

#File Handling
def bank_records():
    a =open("bankRecords.txt","a")
    # if not os.path.exists("bankRecords.txt") or os.path.getsize("bankRecords.txt") == 0:
    with open("bankRecords.txt", "a") as a:
            a.write(f"\nName\tAccount No\tBalance\t\tPassword")

    with open("bankRecords.txt", "a") as a:
        a.write(f"\n{b.name}\t\t{b.acnum}\t\t\t{b.balance}\t\t{b.password}")

#Store
AcountDetails = []

#account function
def get_data(acnum):
    for a in AcountDetails:
        if a.acnum == acnum:
            return a
    return None


while True:
    print("\n========== Bank Management System ==========")
    print("\n1: Open Account")
    print("2: Show Accounts")
    print("3: Credit")
    print("4: Withdrawal")
    print("5: Tranfer")
    print("6: Exit")
    print("==========================================")
    choice = int(input("Choice: "))

    match choice:
        case 1:
            n = int(input("Number of new accounts to open: "))
            for _ in range(n):
                while True:
                    acnum = int(input("Enter a unique account number: "))
                    if get_data(acnum):
                        print("Account already exists! Try another number.")
                    else:
                        break
                b = Bank()
                b.acnum = acnum  # Set unique account number
                b.personDetails()
                AcountDetails.append(b)
                print("Account created successfully.")
                bank_records()

        case 2:
            print("\nName\tAccount no\tBalance")
            for a in AcountDetails:
                a.displayDetails()

        case 3:
            fnum = int(input("Enter account number: "))
            account = []
            for a in AcountDetails:
                if a.acnum == fnum:
                    account = a
                    break
            if account:
                repass = input("Enter password: ")
                if account.password == repass:
                    a.creditMoney()
                else:
                    print("Invalid password...")
            else:
                print("Account not found.Go to the case 1....")
            bank_records()

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
                    a.withdrawMoney()
                else:
                    print("Incorrect password.")
            else:
                print("Account not found.Go to the case 1....")
            bank_records()

        case 5:
            fnum1 = int(input("Enter account number of sender: "))
            fnum2 = int(input("Enter account number of receiver: "))

            sender = get_data(fnum1)
            receiver = get_data(fnum2)

            if sender and receiver:
                repass = input("Enter the Password:")
                if sender.password == repass:
                    amount = int(input("Enter amount to transfer: "))
                    sender.transferMoney(amount, receiver)
                else:
                    print("Invalid Password...")
            else:
                print("Invalid sender or receiver account number...")
            bank_records()

        case 6:
            print("Thank you for using the Bank System. Goodbye!")
            break

        case _:
            print("Invalid choice. Please try again.")