items = [
    ("Product1", 10),("Product2", 5), ("Product3", 15)
    ]

#lambda parameters:expression #lambda functions
items.sort(key=lambda item: item[1])
print(items)

#map functions
prices = list(map(lambda item: item[1], items )) 
print(prices)

#filteredlists
filtered =list(map(lambda item: item[1] >= 10, items ))
print(filtered)

#list_comprehensions
#[expression for item in items] - Syntax 
prices = [item[1] for item in items]
print(prices)

filtered = [item for item in items if item[1] >= 10]
print(filtered)









    