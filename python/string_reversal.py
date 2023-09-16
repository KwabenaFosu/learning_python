# Method 1 - slice method

#str[start:stop:step]
name = "nathaniel"
rname = name[::-1]
print(rname)

#Method 2 - Recursion

def rname(str):
    if len(str) == 0:
        return str
    else:
        return rname(str[1:]) + str[0] # recursive method that skips the first letter and appends 
    
str = "nathaniel"
reverse = (rname(str))
print(reverse)
    

