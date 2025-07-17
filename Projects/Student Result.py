print("\t\t\t\tStudent Result")

# First student
rNo = int(input("Enter the Roll No: "))
name = input("Enter the Name: ")
hindi = int(input("Enter marks in Hindi: "))
guj = int(input("Enter marks in Gujarati: "))
ss = int(input("Enter marks in SS: "))
    
# Calculate min and max
min_marks = hindi
if guj < min_marks:
    min_marks = guj
if ss < min_marks:
    min_marks = ss

max_marks = hindi
if guj > max_marks:
    max_marks = guj
if ss > max_marks:
    max_marks = ss

# Total and percentage
total = hindi + guj + ss
percentage = total / 3

# Grade
if percentage < 33:
    grade = 'F'
else:
    grade = 'P'

# Print result
print("\nrNo\tName\tHindi\tGuj\tSS\tMin\tMax\tTotal\tPercentage\tGrade")
print(f"{rNo}\t{name}\t{hindi}\t{guj}\t{ss}\t{min_marks}\t{max_marks}\t{total}\t{percentage:.2f}\t\t{grade}")
