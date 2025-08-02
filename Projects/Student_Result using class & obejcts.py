class Student:
    #Constructor
    def __init__(self):
        self.rno = 0
        self.name = ""
        self.hindi = 0
        self.gujarati = 0  
        self.ss = 0
        self.total = 0
        self.percentage = 0.0
        self.grade = ""
        self.min_marks = 0
        self.max_marks = 0

    #Input from user
    def inputDetails(self):
        self.rno = int(input("Enter Roll Number: "))
        self.name = input("Enter Student Name: ")
        self.hindi = int(input("Enter marks in Hindi: "))
        self.gujarati = int(input("Enter marks in Gujarati: "))
        self.ss = int(input("Enter marks in Social Science (SS): "))

    #Calculate the Marks
    def calculateResult(self):
        marks = [self.hindi, self.gujarati, self.ss]
        self.min_marks = min(marks)
        self.max_marks = max(marks)
        self.total = sum(marks)
        self.percentage = self.total / len(marks)

        if all(m > 33  for m in marks):
            self.grade = "Pass"
        else:
            self.grade = "Fail"

    #Display the result
    def displayResult(self):
        print("\nResult Summary:\n")
        print("RollNo\tName\tHindi\tGujarati\tSS\tMin\tMax\tTotal\tPercentage\tGrade")
        print(f"{self.rno}\t{self.name}\t{self.hindi}\t{self.gujarati}\t\t{self.ss}\t{self.min_marks}\t{self.max_marks}\t{self.total}\t{self.percentage:.2f}%\t\t{self.grade}")

    #File Handling
    def studentHistory(self):
        with open("Student_Records.txt", "a") as s:
            s.write("\t\t\t\t\t\tStudent Records ")
            s.write(f"\nRoll No\t\tNattme\tHindi\tGujarati\tSS\t\tTotal\tPercentage\tGrade")

        with open("Student_Records.txt", "a") as s:
            s.write(f"\n{self.rno}\t\t\t{self.name}\t\t{self.hindi}\t\t{self.gujarati}\t\t\t{self.ss}\t\t{self.total}\t\t{self.percentage:.2f}%\t\t{self.grade}\n")

# Object
s = Student()

# Main Program
while True:
    print("\n========== Student Result System ==========")
    print("1: Student Details")
    print("2: Calculate Result")
    print("3: Display Result")
    print("4: Exit")
    print("==========================================")
    choice = int(input("Choice: "))

    match choice:
        case 1:
            s.inputDetails()

        case 2:
            s.calculateResult()
            
        case 3:
            s.displayResult()
            s.studentHistory()

        case 4:
            print("Thank you for using the Student Result System. Goodbye!")
            break
        case _:
            print("Invalid Choice. Please try again...")
