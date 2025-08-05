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

name=input("enter name=") 
email=input('enter email=') 
contact=input('enter contact=') 
password=input('enter password=') 

sql="insert into user(name,contact, email, password) values(%s,%s,%s,%s)" 
val=[('haresh','398457','haresh@gmail.com','123456'),('jaydip','345678','jaydip@gmail.com','567')] 
 
mycursor.execute(sql,val) 
mydb.commit() 
 
print(mycursor.rowcount,' record inserted') 
mycursor.close() 