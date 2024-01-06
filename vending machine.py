print( """
__     _______ _   _ ____ ___ _   _  ____  
\ \   / / ____| \ | |  _ \_ _| \ | |/ ___| 
 \ \ / /|  _| |  \| | | | | ||  \| | |  _  
  \ V / | |___| |\  | |_| | || |\  | |_| | 
 __\_/_ |_____|_|_\_|____/___|_| \_|\____| 
|  \/  |  / \  / ___| | | |_ _| \ | | ____|
| |\/| | / _ \| |   | |_| || ||  \| |  _|  
| |  | |/ ___ \ |___|  _  || || |\  | |___ 
|_|  |_/_/   \_\____|_| |_|___|_| \_|_____|
""")

import random

# Initialize the vending machine with lists for snacks and drinks
class FancyVendingMachine:
    def __init__(self):
        self.snacks = {
            1: {"name":    "Chips", "price": 1.50, "quantity": 5},
            2: {"name":     "Mars", "price": 2.50, "quantity": 5},
            3: {"name":     "Oreo", "price": 5.00, "quantity": 5},
            4: {"name":  "Popcorn", "price": 2.00, "quantity": 5},
            5: {"name": "Malteser", "price": 3.50, "quantity": 5}
        }

        self.drinks = {
            1: {"name":     "Soda", "price": 3.50, "quantity": 5},
            2: {"name":    "Water", "price": 2.00, "quantity": 5},
            3: {"name":    "Juice", "price": 4.00, "quantity": 5},
            4: {"name": "Red Bull", "price": 9.75, "quantity": 5},
            5: {"name": "Iced Tea", "price": 7.25, "quantity": 5}
        }

        self.balance = 0.0

# Display the menu with item numbers, names, quantities, and prices
def display_menu(self, menu_name, menu):
    print("\n{} Menu:".format(menu_name))
    print("{:<5} {:<20} {:<10} {:<10}".format("Item", "Name", "Price", "Quantity"))
    
    for idx, item_info in sorted(menu.items()):
        print("{:<5} {:<20} ${:<10.2f} {:<10}".format(
            idx, item_info['name'], item_info['price'], item_info['quantity']))


# Allow the user to insert money into the machine
    def insert_money(self):
        try:
            amount = float(input("\nEnter the amount of money u want: $"))
            if amount > 0:
                self.balance += amount
                print("Balance: ${:.2f}".format(self.balance))
            else:
                print("Please insert a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

# Allow the user to select an item using item codes and handle the purchase within the selected menu
    def select_item(self, menu):
        try:
            if self.balance <= 0:
                print("Please insert money first.")
                return

            item_code = int(input("\nEnter the {} item code to purchase: ".format("Snacks" if menu == self.snacks else "Drinks")))
            item_info = menu.get(item_code)

            if item_info and item_info["quantity"] > 0:
                item_name = item_info["name"]
                purchased_item = item_name
                self.process_purchase(purchased_item, menu, item_code)
                self.suggest_item(purchased_item, menu)
            elif item_info and item_info["quantity"] == 0:
                print("Sorry, {} is out of stock. Please choose another item.".format(item_info['name']))
            else:
                print("Invalid item code. Please select a valid item.")
        except ValueError:
            print("Invalid input. Please enter a valid item code.")

# Process the purchase based on the selected item and deduct the specified price
    def process_purchase(self, item, menu, item_code):
        price = menu[item_code]["price"]
        menu[item_code]["quantity"] -= 1

        if self.balance >= price:
            self.balance -= price
            print("\nEnjoy your {}! Remaining balance: ${:.2f}".format(item, self.balance))
        else:
            print("Insufficient funds. Please insert more money.")

# Suggest a random item from the corresponding list with a suggestion message
    def suggest_item(self, purchased_item, menu):
        category = "drinks" if menu == self.drinks else "snacks"
        suggestion_code = random.choice(list(menu.keys()))
        suggestion = menu[suggestion_code]["name"]
        print("\nHow about trying {} from the {} menu? It goes well with {}!".format(suggestion, category, purchased_item))

# Display the user's current balance
    def check_balance(self):
        print("\nYour current balance is ${:.2f}. Feel free to use it for your next purchase!".format(self.balance))

# Process the return of the user's remaining balance
    def return_change(self):
        change = self.balance
        self.balance = 0
        print("\nReturned change: ${:.2f}. Thank you for using the Fancy Vending Machine!".format(change))

# Initialize the vending machine
def main():
    vending_machine = FancyVendingMachine()

# Display both snacks and drinks menus
    while True:
        vending_machine.display_menu("Snacks", vending_machine.snacks)
        vending_machine.display_menu("Drinks", vending_machine.drinks)

        # Prompt the user for input
        print("\nWelcome to Fancy Vending Machine! Feel free to Buy whatever you want")
        print("1. Insert Money\n2. Select Item to Purchase\n3. Return Change\n4. Check Balance\n5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            vending_machine.insert_money()
        elif choice == 2:
            menu_selection = int(input("Enter the menu you want to select (1 for snacks, 2 for drinks): "))
            menu = vending_machine.snacks if menu_selection == 1 else vending_machine.drinks
            vending_machine.select_item(menu)
        elif choice == 3:
            vending_machine.return_change()
            break  # Exiting the vending machine after returning change
        elif choice == 4:
            vending_machine.check_balance()
        elif choice == 5:
            print("Thank you for using the Fancy Vending Machine. Have a wonderful day!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()