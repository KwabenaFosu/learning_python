import json
from pathlib import Path
employee_list = [
   {"id": 1, "name": "John", "department": "Kitchen"},
   {"id": 2, "name": "Paul", "department": "House Floor"},
   {"id": 3, "name": "Sarah", "department": "Management"},
   {"id": 4, "name": "Lisa", "department": "Cold Storage"},
   {"id": 5, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 6, "name": "Gill", "department": "Cashier"}
]
data =json.dumps(employee_list)
print(data)
Path("/Users/nathanielofosuasiedu/Downloads/Learn/Projects/learning_python/python/files/employee_list.json").write_text(data)


employee_list = json.loads(data)
print(employee_list[1])