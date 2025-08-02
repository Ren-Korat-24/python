import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    port=3307,
    database="ren"
)

print("Connected successfully")

mycursor = mydb.cursor()

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
            n=int(input("Number of account open :"))
            for _ in range(n):
                while True:
                    acnum=int(input("Enter the account number:"))
                    if get_data(acnum):
                        print("Account already exists! Try another number.")
                    else:
                        break
