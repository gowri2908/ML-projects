menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 30,
    'coffee': 20,
    'tea': 10,
    'salad': 60
}

print("Welcome to the Cafe!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs{price}")

order_total = 0

while True:
    item = input('Enter the name of the item you want to order: ').lower()
    if item in menu:
        order_total += menu[item]
        print(f'{item.capitalize()} is added to your order.')
    else:
        print('Sorry, item not available in the menu.')

    more = input('Do you want to add another item to the order? (yes/no): ').lower()
    if more != 'yes':
        break

print(f'Your total bill is: Rs{order_total}')
