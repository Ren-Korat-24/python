sum =0
num= int(input("Enter the Number:"))

while num>0:

    r = num % 10
    sum =sum + r
    num = num // 10

print("Sum = ",sum)

