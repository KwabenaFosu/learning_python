# Working with strings
course_name  = "python programming"
print(len(course_name))
print(course_name[0:3]) #slice a string
print (course_name[-1])
print(course_name[:3])

course = "chemistry \n biology" #starting a text on a new line
print (course)
course = "physics\"maths" #escape sequence
print(course)

course = "\"laser physics"",""optics\"" #escape sequence
print(course)

first_name = "nathaniel"
last_name = "ofosu"
full_name = f"{first_name} {last_name}" #concatenation with f string
print(full_name)
full_name = first_name + " " + last_name
print(full_name)