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
id=input("Enter the number:")

mycursor.execute("DELETE FROM user WHERE id = %s")

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
