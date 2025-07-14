'''
    1 
    2 3 
    4 5 6
    7 8 9 10
    
'''
n=1

for i in range(1,5):
    for j in range(i):
        print(n,end=' ') 
        n += 1
    print()