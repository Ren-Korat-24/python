class Hotel():
    def __init__(self):
        self.total_Room = 100
        self.booked_rooms = []

    def book_room(self, room_no):
        if room_no < 1 or room_no > 100:
            print("Room number must be between 1 and 100.")
        elif room_no in self.booked_rooms:
            print(f"Room {room_no} is already booked.")
        else:
            self.booked_rooms.append(room_no)
            print(f"Room {room_no} has been successfully booked.")

    def show_booked_rooms(self):
        if not self.booked_rooms:
            print("No rooms are booked yet.")
        else:
            print("Booked Rooms:", self.booked_rooms)

    def show_available_room(self):
        available_rooms = [] 
        for i in range(available_rooms):
            if available_rooms in self.booked_rooms:
                print("THis is available")
            else:
                print("Booked Rooms:", self.booked_room)
            

hotel = Hotel()

while True:
    print("\n========== Hotel Management System ==========")
    print("1: Book Room")
    print("2: Booked Rooms")
    print("3: Available Rooms")
    print("4: Exit")
    print("=============================================")

    choice = int(input("Choice: "))

    match choice:
        case 1:
            n = int(input("How many rooms you want? "))
            for i in range(n):
                r1 = input(f"Enter room number {i + 1}: ")
                if r1.isdigit():
                    room_no = int(r1)
                    hotel.book_room(room_no)
                else:
                    print("Please enter a valid room number.")

        case 2:
            hotel.show_booked_rooms()

        case 3:
            hotel.show_available_room()

        case 4:
            print("Thank you for using the Hotel Management System.")
            break

        case _:
            print("Invalid choice. Please select from 1 to 4.")
