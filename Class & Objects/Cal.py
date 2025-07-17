class Cal:
    def add(self,a,b):
        print("Additon:",a+b)
        
    def sub(self):
        print("Substraction:",a-b)
        
    def Mul(self):
        print("\Multiplication:",a*b)
        
    def Div(self):
        print("Divison:",a/b)
        
    def Mod(self):
        print("Modulo:",a%b)
c=Cal()

a=int(input("Enter the A:"))
b=int(input("Enter the B:"))

print("\n========== Bank Management System ==========")
print("Add = 1")
print("Sub = 2")
print("Mul = 3")
print("Div = 4")
print("Module = 5")
print("==========================================")
choice=int(input("Enter the no:"))

if choice==1:
    c.add()

elif choice==2:
    c.sub()


elif choice==3:
    c.Mul()

elif choice==4:
    c.Div()

elif choice==5:
    c.Mod()
