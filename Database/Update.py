import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port=3306,
  database="ren"
)
print("Connected successfully")
 
mycursor=mydb.cursor()

sql = "UPDATE user SET contact = %s WHERE contact = %s"
val = ("9653552136", "35555542")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")