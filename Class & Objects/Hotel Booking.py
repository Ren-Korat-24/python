class Hotel:
    def __init__(self):
        self.hRoom=100
        self.rno = 0

    def bookRoom(self):
        for x in self.rno:
            print(x)
            self.rno+=1

def get_data(rnum):
    for h in Hotel:
        if h.rnum == h.rnum:
            return True
    return None


while True:
    print("\n========== Bank Management System ==========")
    print("1:Book Room")
    print("2:Booked Room")
    print("3:Available Room")
    print("==========================================")
    choice = int(input("Choice: "))

match choice:
    case 1:
        n = int(input("How many rooms you want?"))
        for _ in range(100):
            while True:
                h = Hotel()
                h.bookRoom
                # rnum = int(input("Enter a room number: "))
        #     if h.rno == rnum:
        #         print("Room is not available...")
        #     else:
        #         print("Room is available...")
        # h = Hotel()
        # h.bookRoom()
        # h.append()
        # print("Room Booked succesfully...")
