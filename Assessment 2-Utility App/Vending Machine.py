# Vending Machine Menu
menu = {
    'A1': {'name': 'Cola', 'price': 3.00, 'category': 'Drinks'},
    'A2': {'name': 'Water', 'price': 2.00, 'category': 'Drinks'},
    'A3': {'name': 'Apple Juice', 'price': 5.00, 'category': 'Drinks'},
    'A4': {'name': 'Orange Juice', 'price': 5.00, 'category': 'Drinks'},
    'B1': {'name': 'Chips', 'price': 3.00, 'category': 'Snacks'},
    'B2': {'name': 'Lays', 'price': 3.00, 'category': 'Snacks'},
    'B3': {'name': 'Biscuit', 'price': 2.00, 'category': 'Snacks'},
    'C1': {'name': 'Coffee', 'price': 2.00, 'category': 'Hot Drinks'},
    'C2': {'name': 'Tea', 'price': 2.00, 'category': 'Hot Drinks'},
}

# Display Menu
print("Welcome to the Vending Machine!")
print("Menu:")
for code, details in menu.items():
    print(f"Code: {code} - Item: {details['name']} - Price: ${details['price']}")

# User Input
selection = input("Enter the item code you want to purchase: ")

# Money Input
money_inserted = float(input("Please insert money: $"))

# Processing Selection
if selection in menu:
    selected_item = menu[selection]['name']
    price = menu[selection]['price']

    if money_inserted >= price:
        change = money_inserted - price
        print(f"Dispensing {selected_item}. Thank you for shopping with us. Have a great day!")
        print(f"Change: ${change:.2f}")
    else:
        print("Insufficient funds. Money refunded.")
else:
    print("Invalid selection. Please try again.")
