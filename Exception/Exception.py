a=10
b=0

#First try..
try:
    print("Div",a/b)

#If try is not working..
except ZeroDivisionError:
    print("Can't Divide by Zero..")

#If catch is not working but try working
else:
    print("Result",a+b)

#Is the end of the code..
finally:
    print("Execution Completed...")