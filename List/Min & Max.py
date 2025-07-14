my_list = [0] * 100  # fixed-size list
size = 0

n = int(input("Enter the Number you want : "))

if n > 100 or n < 1:
    print("Invalid number of values...")
else:
    print("Enter",n,"values:")
    i = 0
    while i < n:
        val = int(input("Enter value ","{i + 1}: "))
        my_list[i] = val
        size += 1
        i += 1

    #Minimum
    min_val = my_list[0]
    i = 1
    while i < size:
        if my_list[i] < min_val:
            min_val = my_list[i]
        i += 1

    #Maximum
    max_val = my_list[0]
    i = 1
    while i < size:
        if my_list[i] > max_val:
            max_val = my_list[i]
        i += 1

    print(f"\nMinimum value: {min_val}")
    print(f"Maximum value: {max_val}")
