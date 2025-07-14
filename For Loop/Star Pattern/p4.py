'''
    *     
    *     
* * * * * 
    *     
    *     

'''

r = 5
for i in range(1, r+1):
    for j in range(1, r+1):
        if i == (r+1)//2 or j == (r+1)//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
