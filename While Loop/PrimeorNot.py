num = int(input("Enter the Number:"))
i=2 
flag = 0

if num <= 1:
    print("Not a Prime Number")
else:
    while i < num:
        if num % i == 0:
            flag = 1
            break
        i += 1

    if flag == 0:
        print("Prime Number")
    else:
        print("Not a Prime Number")