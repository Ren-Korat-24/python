class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price


class Cart:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def remove_items(self, pid):
        for item in self.items:
            if item.pid == pid:
                self.items.remove(item)
                print(f"{item.name} removed from cart.")
                return
        print("Item not found in cart.")

    def view_cart(self):
        if not self.items:
            print("\n🛒 Cart is empty.")
            return

        print(f"\n🛒 Cart Items for {self.name}:")
        total = 0
        for item in self.items:
            print(f"- {item.name} ₹ {item.price}")
            total += item.price
        print(f"Total Price: ₹{total}")

    def save_cart(self):
        if not self.items:
            print("Cart is empty. Nothing to save.")
            return

        filename = f"cart_{self.name.lower().replace(' ', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"🧾 Cart Summary for {self.name}:\n")
            total = 0
            for item in self.items:
                f.write(f"- {item.name} ₹{item.price}\n")
                total += item.price
            f.write(f"Total: ₹{total}\n")
        print(f"✅ Cart saved to '{filename}'.")
        

# Ask for customer name
customer_name = input("Enter your name: ")
cart = Cart(customer_name)

# Sample products
products = [
    Product(1, "Laptop", 55000),
    Product(2, "Headphones", 1500),
    Product(3, "Mouse", 500),
    Product(4, "Keyboard", 800),
    Product(5, "Monitor", 7000),
]

while True:
    print(f"\n========== Online Shopping Menu ({cart.name}) ==========")
    print("1: Show Products")
    print("2: Add to Cart")
    print("3: Remove from Cart")
    print("4: View Cart")
    print("5: Save & Exit")
    print("==========================================")
    choice = input("Choice: ")

    match choice:
        case "1":
            print("\n📦 Available Products:")
            for p in products:
                print(f"{p.pid}. {p.name} - ₹ {p.price}")

        case "2":
            pid_input = input("Enter Product ID to add: ")
            if pid_input.isdigit():
                pid = int(pid_input)
                found = next((p for p in products if p.pid == pid), None)
                if found:
                    cart.add_items(found)
                else:
                    print("Invalid product ID.")
            else:
                print("Please enter a valid number.")

        case "3":
            pid_input = input("Enter Product ID to remove: ")
            if pid_input.isdigit():
                pid = int(pid_input)
                cart.remove_items(pid)
            else:
                print("Please enter a valid number.")

        case "4":
            cart.view_cart()

        case "5":
            cart.save_cart()
            print("\n🛍️ Thank you for shopping with us! Goodbye.")
            break

        case _:
            print("⚠️ Invalid choice. Please try again.")
