rev = 0
num = int(input("Enter the Number:"))
temp = num

while num>0:
    r = num % 10
    rev = rev * 10 + r 
    num = num // 10

if temp == rev:
    print("The number is a Palindrome.")
else:
    print("The number is nOt a Palindrome.")