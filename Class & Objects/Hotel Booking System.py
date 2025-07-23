class Hotel():
    def __init__(self):
        self.total_Room = 100
        self.booked_rooms = {}

    def book_room(self, room_no,customer_name):
        if room_no < 1 or room_no > 100:
            print("Room number must be between 1 and 100.")
        elif room_no in self.booked_rooms:
            print(f"Room {room_no} is already booked.")
        else:
            self.booked_rooms[room_no]=customer_name
            print(f"Room {room_no} has been successfully booked for {customer_name}.")

    def show_booked_rooms(self):
        if not self.booked_rooms:
            print("No rooms are booked yet.")
        else:
            print("Booked Rooms:", self.booked_rooms)

    def show_available_room(self):
        available_rooms = []
        for room in range(1, self.total_Room + 1):
            if room not in self.booked_rooms:
             available_rooms.append(room_no)

        if len(available_rooms) == 0:
            print("No available rooms.")
        else:
            print("Available Rooms:", available_rooms)
        
    def cancel_booking(self,room_no):
        if room_no in self.booked_rooms:
            del self.booked_rooms[room_no]
            print(f"Booking for Room {room_no} has been cancelled.")
        else:
            print(f"Room {room_no} is not booked.")

    def hotel_records(self):
        with open("Hotel_Records.txt","a") as hotel:
            hotel.write("\t\t\t\t\t\tHotel Records ")
            hotel.write(f"\n{self.book_room},{self.booked_rooms}")

hotel = Hotel()

while True:
    print("\n========== Hotel Management System ==========")
    print("1: Book Room")
    print("2: Booked Rooms")
    print("3: Cancel Rooms")
    print("4: Exit")
    print("=============================================")

    choice = int(input("Choice: "))

    match choice:
        case 1:
            n = int(input("How many rooms you want? "))
            for i in range(n):
                r1 = input(f"Enter room number {i + 1}: ")
                customer_name=input("Enter the name:")
                if r1.isdigit():
                    room_no = int(r1)
                    hotel.book_room(room_no,customer_name)
                else:
                    print("Please enter a valid room number.")
            hotel.hotel_records()

        case 2:
            hotel.show_booked_rooms()
            hotel.show_available_room()
            hotel.hotel_records()
            
        case 3:
            hotel.cancel_booking(room_no)
            hotel.hotel_records()

        case 4:
            print("Thank you for using the Hotel Management System.")
            break

        case _:
            print("Invalid choice. Please select from 1 to 4.")
