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

for x in menu:
    print(menu)
#subtotal of price of items
order = 0.0
for k,v in menu.items():
    order += v["price"]
    order = round(order, 2)
subtotal = print(order)

#calculate the tax on total bill
def calculate_tax():
    tax = 0.15 * float(subtotal)
    return tax
print(calculate_tax())


#summarize order
def summarize_order(order):
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)

    names = []
    for i in order:
        names.append(i['name'])
    return names, total





def calculate_subtotal(order):
    subtotal = 0
    for i in order:   
        subtotal += i['price']
    subtotal = round(subtotal, 2)
print("Subtotal for the order is: " + str(subtotal))


