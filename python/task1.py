menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def print_order(order):                       # This function will print out the items in an order
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


def display_menu():                           # This function displays the menu
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()



def take_order():                            # This function creates an order by prompting the user to select menu items
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order



def calculate_subtotal(order):              # Calculates the subtotal of an order
    print('Calculating bill subtotal...')
    subtotal = 0
    for i in order:
        subtotal += i['price']
    subtotal = round(subtotal, 2)
    print("Subtotal for the order is: " + str(subtotal))
    return subtotal

    raise NotImplementedError()



def calculate_tax(subtotal):                # Calculates the tax on the subtotatal of an order
    print('Calculating tax from subtotal...')
    tax = subtotal * 0.15
    tax = round(tax, 2)
    print("Tax for the order is: " + str(tax))
    return tax

    raise NotImplementedError()

def summarize_order(order):                # Function that summarizes order
    print_order(order)
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)

    names = []
    for i in order:
        names.append(i['name'])
    return names, total

    raise NotImplementedError()

'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''
def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(order)

if __name__ == "__main__":
    main()










