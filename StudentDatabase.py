import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", port=3307, database="ren"
)

print("Connected successfully")
mycursor = mydb.cursor()

# User Input
# rollNo=int(input("Enter the roll no : "))
name = input("Enter Name : ")
hindi = int(input("Enter the Hindi : "))
english = int(input("Enter the English : "))
gujarati = int(input("Enter the gujarati : "))  
ss = int(input("Enter the SS : "))
maths = int(input("Enter the Maths : "))

# Minimum
min_marks = hindi
if english < min_marks:
    min_marks = english
if gujarati < min_marks:
    min_marks = gujarati
if ss < min_marks:
    min_marks = ss
if maths < min_marks:
    min_marks = maths

# Maximum
max_marks = hindi
if english > max_marks:
    max_marks = english
if gujarati > max_marks:
    max_marks = gujarati
if ss > max_marks:
    max_marks = ss
if maths > max_marks:
    max_marks = maths

# Total & Percentage
total = hindi + english + gujarati + ss + maths
percentage = total / 5

# Grade
if hindi < 33 or english < 33 or gujarati < 33 or ss < 33 or maths < 33:
    grade = "F"
else:
    grade = "P"

# Result
print("\nName\tHindi\tenglish\t\tGujarati\tSS\tmaths\tMin\tMax\tTotal\tPercentage\tGrade")
print(
    f"\n{name}\t{hindi}\t{english}\t\t{gujarati}\t\t{ss}\t{maths}\t{min_marks}\t{max_marks}\t{total}\t{percentage:.2f}\t\t{grade}"
)

sql = "insert into admin(name,hindi,english,gujarati,ss,maths,min,max,total,percentage,grade) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

val = (
    name,
    hindi,
    english,
    gujarati,
    ss,
    maths,
    min_marks,
    max_marks,
    total,
    percentage,
    grade,
)

mycursor.execute(sql, val)

mydb.commit()

print("Succesfully data inserted...")
