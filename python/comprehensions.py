#List Comprehensions
# Syntax - [ <expression> for x in <sequence> if <condition>] 

data = [2,3,5,7,11,13,17,19,23,29,31]
data = [x+3 for x in data]
print("Updating the list: ", data)

new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

sevenx = [x for x in data if x%7 == 0 ]
print("Divisible by four", sevenx)



# Dictionary Comprehensions
# Syntax - dict = { key:value for key, value in <sequence> if <condition> } 
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

#Using one input list
numberdict = {x:x*2 for x in number}
print("Number Dictionary: ", numberdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)} #Zip function combines both lists
print("Using two lists: ", months_dict)


#Set comprehension
# Syntax similar to lists only difference is curly brackets
set_data = {2,3,5,7,11,13,17,19,23,29,31}
set2_data = {a for a in set_data}
print ("Sets comprehension :", set2_data)

set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)