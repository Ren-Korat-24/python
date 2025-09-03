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

#Show tables in database
mycursor.execute("SHOW TABLES")
for x in mycursor: 
    print(x) 

