my_list = [0] * 100  # fixed-size list
size = 0  # number of actual inserted elements

while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Exit")
    choice = input("Enter your choice: ")

    #Insert
    if choice == '1':
        value = int(input("Enter value to insert: "))
        position = int(input("Enter position (0-based index): "))

        if position < 0 or position > size:
            print("Invalid position!")
        elif size >= len(my_list):
            print("List is full!")
        else:
            i = size
            while i > position:
                my_list[i] = my_list[i - 1]
                i -= 1
            my_list[position] = value
            size += 1
            print(f"Inserted {value} at position {position}.")

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
