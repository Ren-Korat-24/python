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
mycursor.execute("ALTER TABLE user ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 