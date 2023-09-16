def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

ans = divide_by(12,0)
print(ans)


try:
    items = [1,2,3,4,5]
    item = items[6]
    print(item)
except: 
    print("The index does not exist in the list.")


#file exception
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")  

