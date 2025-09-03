import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port=3306,
  database="ren"
)

print("Connected successfully")

mycursor = mydb.cursor()
id=input("Enter the id no:")
sql= "DELETE FROM user WHERE id = %s"
mycursor.execute(sql,(id,))

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
