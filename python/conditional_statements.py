count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'We have a count of {count} even numbers ')



num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0
for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print("Number found at 36 is:", x) 
        break
print(count)

nums = 18
for i in nums:
    print(i)