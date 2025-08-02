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


name = input("Enter Name : ")
email = input("Enter Email : ")
contact = input("Enter Contact : ")

# sql = "insert into user(name,email,contact)values('ren','ren@gmail.com','1234')"
sql = "insert into user(name,email,contact)values(%s,%s,%s)"
# val = ('raj','raj@gmail.com','raj123')
val = (name,email,contact)

mycursor.execute(sql,val)

mydb.commit()

print("data inserted")


