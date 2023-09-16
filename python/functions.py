def total_sum(*numbers): #xargs
    count = 0
    for number in numbers:
        count = count + number
        #count += number 
    return count

print(total_sum(1,2,3,4))


#fizzbuzz challenge
#First try
def fizz_buzz(input):
     if (input % 3 == 0) and (input % 5 == 0):
          return "FizzBuzz"
     elif input % 5 == 0:
          return "Buzz"
     elif input % 3 == 0:
          return "Fizz"
     else:
          return input
     

print(fizz_buzz(15))

#Optimized way
def fizz_buzz(input):
        if (input % 3 == 0) and (input % 5 == 0):
            return "FizzBuzz"
        if input % 3 == 0:
            return "Fizz"
        if input % 5 == 0:
            return "Buzz"
        
        else:
            return input


print(fizz_buzz(46))
    



for i in range (1,4):
    print(i)
