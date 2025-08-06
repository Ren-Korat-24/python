import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port=3307,
  database="ren"
)

mycursor = mydb.cursor()

sql = "DROP TABLE user where id=2"

mycursor.execute(sql)
