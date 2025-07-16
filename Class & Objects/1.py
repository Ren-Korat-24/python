#Class
class first :
    #Constructor
    def __init__(self):
        print("Constructor called")

    #Functions
    def getData(self,a,b):
        self.a=a
        self.b=b
        print("A:",a,"B",b)
    
    def setData(self):

        print("A:",self.a,"B:",self.b)

#Objects
f=first()
f.getData(10,20)
f.setData()