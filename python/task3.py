# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp


# Task 1
def to_mod_list(employee_list):     #Modifies the employee list of dictionaries into list of employee-department strings"""
    map(mod, employee_list)
    map_emp = map(mod, employee_list)
    return list(map_emp)



#Task 2

def generate_usernames(mod_list):    #Generates a list of usernames 
   emp_list = [x.replace(" ", "_") for x in mod_list]
   return emp_list


# Task 3
def map_id_to_initial(employee_list): # Dictionary that maps employee id to first initial.
   employee_dict = {employee["name"][0]:employee["id"] for employee in employee_list}
   return employee_dict

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()