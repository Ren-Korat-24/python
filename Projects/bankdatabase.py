import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", port=3307, database="ren"
)

print("Connected successfully")


class Bank:
    # Constructor
    def __init__(self):
        self.name = ""
        self.acnum = 0
        self.password = ""
        self.balance = 0

    # Basic Details
    def personDetails(self):
        self.name = input("Enter the name: ")
        # check Passoword
        while True:
            self.password = input("Enter the Password (min 8 characters): ")
            if len(self.password) >= 8:
                break
            else:
                print("Password is too short...")
        # Check Balance
        while True:
            self.balance = int(input("Enter Amount (minimum 2000): "))
            if self.balance >= 2000:
                break
            else:
                self.balance = int(input("Enter the number "))
                print("Minimum deposit is 2000!")

    # Display
    def displayDetails(self):
        print(f"{self.name}\t{self.acnum}\t\t{self.balance}")

    # Credit
    def creditMoney(self):
        money = int(input("Enter the Amount to deposit: "))
        self.balance += money
        print("Credit Successful.Updated balance:", self.balance)

    # Debit
    def withdrawMoney(self):
        money = int(input("Enter the Amount to withdraw: "))
        if money > self.balance:
            print("Insufficient Balance...")
        else:
            self.balance -= money
            print("Withdrawal Successful...\nRemaining Balance:", self.balance)

    # Tranfer
    def transferMoney(self, amount, receiver):
        if amount > self.balance:
            print("Insufficient Balance.Transfer Failde..")
        else:
            self.balance -= amount
            receiver.balance += amount
            print(f"₹{amount} transferred successfully to Account {receiver.acnum}")
            print(f"Your remaining balance: ₹{self.balance}")

    # def get_account(self):
    #     mycursor = mydb.cursor()
    #     sql="insert into bank(acnum,name,password,balance)values(%s,%s,%s,%s)"
    #     val =(acnum,self.name,self.password,self.balance)

    #     mycursor.execute(sql,val)
    #     mydb.commit()
    # print("data inserted")


# File Handling
def bank_records():
    a = open("bankRecords.txt", "a")
    # if not os.path.exists("bankRecords.txt") or os.path.getsize("bankRecords.txt") == 0:
    with open("bankRecords.txt", "a") as a:
        a.write(f"\nName\tAccount No\tBalance\t\tPassword")

    with open("bankRecords.txt", "a") as a:
        a.write(f"\n{b.name}\t\t{b.acnum}\t\t\t{b.balance}\t\t{b.password}")


# Store
AcountDetails = []

# account function
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
                mycursor = mydb.cursor()
                sql = "insert into bank(acnum,name,password,balance)values(%s,%s,%s,%s)"
                val = (b.acnum, b.name, b.password, b.balance)
                mycursor.execute(sql, val)
                mydb.commit()
                print("Account created successfully")

        case 2:
            print("\nName\tAccount no\tBalance")
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM bank")

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)
            print("Show The Account Details..")

        case 3:
            fnum = int(input("Enter account number: "))
            mycursor = mydb.cursor()
            sql = "SELECT * FROM bank WHERE acnum = %s"
            mycursor.execute(sql, (fnum,)) 
            myresult = mycursor.fetchall() 
            repass = input("Enter password: ")

            if myresult:
                if myresult[2] == repass: 
                    print("Login Successfully...")
                    print("Account Details:", myresult)
                    b = Bank()
                    b.acnum = myresult[0]
                    b.name = myresult[1]
                    b.password = myresult[2]
                    b.balance = myresult[3]
                    b.creditMoney()

                    update_cursor = mydb.cursor()
                    update_cursor.execute("UPDATE bank SET balance = %s WHERE acnum = %s", (b.balance, b.acnum))
                    mydb.commit()
                    print("Balance updated in database.")
                else:
                    print("Invalid password.")
            else:
                print("Account not found.")


        case 4:
            fnum = int(input("Enter account number: "))
            mycursor = mydb.cursor()
            sql = "SELECT * FROM bank WHERE acnum = %s"
            mycursor.execute(sql, (fnum,))
            myresult = mycursor.fetchall()
            if myresult:
                repass = input("Enter password: ")
                if myresult[2] == repass:
                    print("Login Successfully...")
                    print("Account Details:", myresult)
                    b = Bank()
                    b.acnum = myresult[0]
                    b.name = myresult[1]
                    b.password = myresult[2]
                    b.balance = myresult[3]
                    b.withdrawMoney()
                    update_cursor = mydb.cursor()
                    update_cursor.execute("UPDATE bank SET balance = %s WHERE acnum = %s", (b.balance, b.acnum))
                    mydb.commit()
                    print("Balance updated in database.")
                else:
                    print("Invalid password.")
            else:
                print("Account not found.")

        case 5:
            fnum1 = int(input("Enter account number of sender: "))
            fnum2 = int(input("Enter account number of receiver: "))
            mycursor = mydb.cursor()

            sender = get_data(fnum1)
            sql = ("SELECT * FROM bank WHERE acnum = %s")
            mycursor.execute(sql, (fnum1,))
            sender_data = mycursor.fetchall()

            receiver = get_data(fnum2)
            sql = ("SELECT * FROM bank WHERE acnum = %s")
            mycursor.execute(sql, (fnum2,))
            receiver_data = mycursor.fetchall()

            if sender_data and receiver_data:
                repass = input("Enter the Password:")
                if sender_data[2] == repass:
                    amount = int(input("Enter amount to transfer: "))
                    sender = Bank()
                    sender.acnum=sender_data[0]
                    sender.name=sender_data[1]
                    sender.password=sender_data[2]
                    sender.balance=sender_data[3]

                    receiver = Bank()
                    receiver.acnum=receiver_data[0]
                    receiver.name=receiver_data[1]
                    receiver.password=receiver_data[2]
                    receiver.balance=receiver_data[3]

                    sender.transferMoney(amount, receiver)
                    update_cursor = mydb.cursor()
                    update_cursor.execute("UPDATE bank SET balance = %s WHERE acnum = %s", (sender.balance, sender.acnum))
                    update_cursor.execute("UPDATE bank SET balance = %s WHERE acnum = %s", (receiver.balance, receiver.acnum))
                    mydb.commit()
                else:
                    print("Invalid Password...")
            else:
                print("Invalid sender or receiver account number...")


        case 6:
            print("Thank you for using the Bank System. Goodbye!")
            break

        case _:
            print("Invalid choice. Please try again.")
    