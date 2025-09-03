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
mycursor.execute("SELECT * FROM user LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)