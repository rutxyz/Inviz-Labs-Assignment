from fastapi import APIRouter, HTTPException
from typing import List
from models import Property, PropertyCreate, PropertyUpdate, City
from database import get_database
from bson import ObjectId

router = APIRouter()

db = get_database()

@router.post("/create_new_property", response_model=List[Property])
def create_new_property(property: PropertyCreate):
    new_property = property.dict()
    result = db.properties.insert_one(new_property)
    new_property["property_id"] = str(result.inserted_id)
    return [{"property_id": str(prop["_id"]), "name": prop["name"], "address": prop["address"], "city": prop["city"], "state": prop["state"]} for prop in db.properties.find()]

@router.get("/fetch_property_details", response_model=List[Property])
def fetch_property_details(city: str):
    properties = list(db.properties.find({"city": city}))
    if not properties:
        raise HTTPException(status_code=404, detail="Properties not found")
    return [{"property_id": str(prop["_id"]), "name": prop["name"], "address": prop["address"], "city": prop["city"], "state": prop["state"]} for prop in properties]

@router.put("/update_property_details", response_model=List[Property])
def update_property_details(property: PropertyUpdate):
    property_id = property.property_id
    if not ObjectId.is_valid(property_id):
        raise HTTPException(status_code=400, detail="Invalid property ID")
    updated_property = property.dict()
    db.properties.update_one({"_id": ObjectId(property_id)}, {"$set": updated_property})
    return [{"property_id": str(prop["_id"]), "name": prop["name"], "address": prop["address"], "city": prop["city"], "state": prop["state"]} for prop in db.properties.find()]

@router.get("/find_cities_by_state", response_model=List[str])
def find_cities_by_state(state: str):
    cities = db.properties.distinct("city", {"state": state})
    return cities

@router.get("/find_similar_properties", response_model=List[Property])
def find_similar_properties(property_id: str):
    if not ObjectId.is_valid(property_id):
        raise HTTPException(status_code=400, detail="Invalid property ID")
    property = db.properties.find_one({"_id": ObjectId(property_id)})
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    city = property["city"]
    similar_properties = list(db.properties.find({"city": city}))
    return [{"property_id": str(prop["_id"]), "name": prop["name"], "address": prop["address"], "city": prop["city"], "state": prop["state"]} for prop in similar_properties]
