import sqlite3
from pathlib import Path
import json

employees = json.loads(Path("/Users/nathanielofosuasiedu/Downloads/Learn/Projects/learning_python/python/files/employee_list.json").read_text())

'''with sqlite3.connect("empldb") as connection:
    command = "INSERT INTO Employees VALUES (?,?,?)"
    for employee in employees:
        connection.execute(command, tuple(employee.values()))
        connection.commit'''

with sqlite3.connect("empldb") as connection:
    command = "SELECT * FROM Employees"   #returns a cursor
    cursor = connection.execute(command)
    employees = cursor.fetchall()
    print(employees)



