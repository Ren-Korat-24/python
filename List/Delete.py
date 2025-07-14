my_list = [10, 20, 30, 40, 50]  
size = 5  # number of size

while True:
    print("\n1. Delete")
    print("2. Display")
    print("3. Exit")
    choice = input("Enter your choice: ")

    #Delet
    if choice == '1':  
        if size == 0:
            print("List  empty.")
        else:
            position = int(input("Enter position to delete from (0-based index): "))
            if position < 0 or position >= size:
                print("Invalid position!")
            else:
                deleted_value = my_list[position]
                i = position
                while i < size - 1:
                    my_list[i] = my_list[i + 1]
                    i += 1
                size -= 1
                print("Deleted value ",deleted_value ,"from position",position)

    #Display
    elif choice == '2':
        if size == 0:
            print("List is empty.")
        else:
            print("Current List: ", end="")
            i = 0
            while i < size:
                print(my_list[i], end=" ")
                i += 1
            print()
    #Exit
    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
