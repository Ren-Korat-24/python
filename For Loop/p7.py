'''
                 1
                212
               32123
              4321234



'''
n = 4  # Number of rows

for i in range(1, n+1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print decreasing part
    for j in range(i, 0, -1):
        print(j, end="")

    # Print increasing part
    for j in range(2, i+1):
        print(j, end="")

    print()  # New line

