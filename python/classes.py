# Understanding classes
class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it. '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
house = House()
print(house.num_rooms)
print(House.num_rooms)

house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)


#Custom objects
# Define class MyFirstClass
class MyFirstClass:
    print("Who wrote this?")
    # Define string variable called index
    index = "Author-Book"
    
    # Define function hand_list()
    def handlist(self,philosopher,book):
        print(MyFirstClass.index)
    
        # variable + “ wrote the book: ” + variable
        print(f'{philosopher} wrote the book: {book}')
        

# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.handlist("Sun Tzu", "The Art of War")



