a=int(input("Enter the A="))
b=int(input("Enter the B="))

c=int(input("Choose the Case="))

match c:
   
    case 1:
        print("Additons:",a+b)
    case 2:
       print("Sub=",a-b)
    case 3:
        print("Mul=",a*b)    
    case 4:
        print("Div=",a/b)
    case 5:
        print("Mod=",a%b)    
    case _:
        print("Not Arithmetic..") 
        