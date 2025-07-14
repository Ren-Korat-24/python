num = int(input("Enter the Number:"))
r=0
temp=num

while num>0:
    rem = num % 10
    r = r + rem*rem*rem
    num = int(num/10)

print(r)

if temp == r:
    print("This Number is Armstrong Number : ",temp)
else:
    print("This Number is not Armstrong Number : ",temp)