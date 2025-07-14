a=0
b=1
count =0
total =0

n = int(input("Enter the Number:"))
while count< n:
    print(a,end=' ')
    total += a
    c =a + b
    a = b
    b = c
    count +=1

print("\nTotal Sum Of Fibonancci Series =",total)