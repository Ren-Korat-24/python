class Person:   
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def personDetails(self):
        print("Hello, my name is",self.name,",I am a",self.age,"Old")
        
P1=Person("John",36)
# print(P1.name)
# print(P1.age)
P1.personDetails()
    
