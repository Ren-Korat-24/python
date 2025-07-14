days=int(input("Enter the You want name of days:"))

match days:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thurday")
        case 5:
            print("Friday") 
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Not a Week")