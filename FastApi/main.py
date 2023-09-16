from lib2to3.pgen2 import driver
from tkinter import N
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Drivers = { 1: {'name': 'Kwame', 'car_model': 'Daewoo Matiz', 'car_registration': 'GW 2017-19'},
            2: {'name': 'Kofi', 'car_model': 'Kia Picanto', 'car_registration': 'GW 318-18'}}

##GET METHOD(Get driver information)
@app.get("/get-driver/{driver_id}")
def get_driver(driver_id: int):
    return Drivers[driver_id]

@app.get("/get-by-name")
def get_driver(name: Optional[str] = None,):
    for driver_id in Drivers:
        if Drivers[driver_id]['name'] == name:
            return Drivers[driver_id]
    return {"Data" : "Not Found"}   

#POST METHOD(Create new driver information)
class Driver(BaseModel):
    name: str
    car_model: str
    car_registration: str

@app.post("/create-driver/{driver_id}") 
def create_driver(driver_id : int, driver : Driver):
    if driver_id in Drivers:
        return {"Error": "Driver exists"}

    Drivers[driver_id] = driver
    return Drivers[driver_id]    

#UPDATE METHOD (Update driver information)
class Update_Driver(BaseModel):
    name: Optional[str] = None
    car_model: Optional[str] = None
    car_registration: Optional[str] = None

@app.put("/update-driver/{driver_id}")
def update_driver(driver_id: int, driver : Update_Driver):
    if driver_id not in Drivers:
        return {"Error": "Driver Exists"}
        
    if driver.name != None:
        Drivers[driver_id].name = driver.name 
   
    if driver.car_model != None:
        Drivers[driver_id].car_model = driver.car_model
     
    if driver.car_registration != None:
        Drivers[driver_id].car_registration = driver.car_registration

    return Drivers[driver_id]   

#DELETE METHOD (delete driver information)
@app.delete("/delete-driver/{driver_id}")
def delete_driver(driver_id : str):
    if driver_id not in Drivers:
        return{"Error" : "Driver does not exist"}
    del Drivers[driver_id]
    return{"Message" : "Driver deleted"}



