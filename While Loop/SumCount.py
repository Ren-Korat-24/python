count =0
num=int(input("Enter the Number="))

if num==0:
    count==1
else:   
    while num > 0:
        num = num // 10
        count += 1

print("Totoal Sum is : ",count)