import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port=3307,
  database="ren"
)
print("Connected successfully")
 
mycursor=mydb.cursor() 
 
mycursor.execute("SELECT * FROM user WHERE email ='email'") 
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
