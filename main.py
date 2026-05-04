from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
# Instance Creation
app = FastAPI() 

# Dictionary containing parents id and their information to test 
parents = {
    101: {
        "name": "Garuba Abdulhammed Olohuntoyin",
        "gender": "male",
        "age": 50,
        "Relationship": "Father"
    },
    102: {
        "name": "Abdulhammed Omowunmi Lateefat",
        "gender": "female",
        "age": 45,
        "relationship": "Mother"
    },
    103: {
        "name": "Yusuf Ganiyat Romoke",
        "gender": "female",
        "age": 40,
        "relationship": "Mother"
    }
}

#Base Model for Creating Using the POST
class Parents(BaseModel):
    name: str
    gender: str
    age: int
    relationship: str

class UpdateParent(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    relationship: Optional[str] = None

#Using GET to retrieve information of parents using their ID
@app.get("/get-parents/{parents_id}") 
def get_student(parents_id: int = Path(description="Your ID to check your parents information", gt=100, lt=200)):
    if parents_id not in parents:
        return {"Error": "Parent does not Exists"}
    return parents[parents_id]

# Using query to retrieve information of parents using their name
@app.get("/get-by-name")
def get_parent(name: Optional[str] = None):
    name = name.lower()
    for parent_id, parent_data in parents.items():
        if name in parent_data["name"].lower():
            return parent_data
        else:
            return {"Data": "Not found"}
    
# Using POST method with BaseModel for parents to create and input their information
@app.post("/create-parents/{parent_id}")
def create_parent(parent_id: int, parent: Parents):
    if parent_id in parents:
        return {"Error": "Parent exists"}
    
    parents[parent_id] = parent
    return parents[parent_id]

#Using PUT method with BaseModel to Update parents information with existing ID's
@app.put("/update-parent/{parent_id}")
def update_parent(parent_id: int, parent: UpdateParent):
    if parent_id not in parents:
        return {"Error": "Parent does not Exists"}
    
    if parent.name != None:
        parents[parent_id].name = parent.name
    if parent.gender != None:
        parents[parent_id].gender = parent.gender
    if parent.age != None:
        parents[parent_id].age = parent.age
    if parent.relationship != None:
        parents[parent_id].relationship = parent.relationship
    return parents[parent_id]

#Using Delete Method to delete and remove parents informatiob directly fully.
@app.delete("/delete-parent/{parent_id}")
def delete_parent(parent_id: int):
    if parent_id not in parents:
        return {"Error" : "Parent does not Exits"}
    
    del parents[parent_id]
    return {"Message": "Deleted Successfully"}


""" This is a summary of the methods in FastAPI with their usage
We have 4 basic methods:
1) GET : to retrive data either from the database or any other place 
(example: when users are login in to a website it fetchs their data and then check if the same with what the user inputted)
2) POST : to create a new data (example: when users are signng up to create an account on a website )
3) PUT : to update data in the database (example: when users change their name or username on an app or website)
4) DELETE : to delete data simply from the database (example: users deleting their account)

