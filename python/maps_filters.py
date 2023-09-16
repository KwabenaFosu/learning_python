menu = ['espresso','latte','campiom','americano','cortado', 'americano','custard','cocoboko']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee 
    
#map function -  takes all objects in a list and allows an applied function
#syntax map(function,list)
map(find_coffee,menu)
map_menu = map(find_coffee, menu)
#print(list(map_menu))
for x in map_menu:
    print(list(map_menu))


#filterfunction- takes all values and creates a new list with the filtered values
#syntax- filter(function,list)
filter(find_coffee, menu)
filter_menu = filter(find_coffee, menu)
for x in filter_menu:
    print(list(filter_menu))


