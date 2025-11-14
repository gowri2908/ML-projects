#define the menu of cafe
menu={'pizza':40,
      'pasta':50,
      'burger':30,
      'coffee':20,
      'tea':10,
      'salad':60
      }

print("Welcome to the Cafe!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs{price}")

#take order from customer
order_total=0
item1=input('enter the name of the item you want to order: ').lower()
if item1 in menu:
    order_total+=menu[item1]
    print(f'{item1} is added to your order')
else:
    print('sorry item not available in the menu')

item2=input('Do you want to add another item in the order? (yes/no): ').lower()
if item2=='yes':
    item2=input('enter the name of the item you want to order: ').lower()
    if item2 in menu:
        order_total+=menu[item2]
        print(f'{item2} is added to your order')
    else:
        print('sorry item not available in the menu')

#calculate total bill
print(f'Your total bill is: Rs{order_total}')

