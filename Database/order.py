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

sql = "SELECT * FROM user ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)