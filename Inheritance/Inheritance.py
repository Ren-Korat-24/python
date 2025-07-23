class first:
    def setdata(self,x,y):
        self.x=x
        self.y=y
       
    def add(self):
        print("ADD",self.x+self.y)

class two(first):
    def getdata(self):
        print("A:",self.x,"B:",self.y)
    
t =two()
t.setdata(20,30)
t.add()
t.getdata()