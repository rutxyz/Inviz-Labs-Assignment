from pydantic import BaseModel
from typing import List, Optional

class PropertyCreate(BaseModel):
    name: str
    address: str
    city: str
    state: str

class PropertyUpdate(BaseModel):
    property_id: str
    name: str
    address: str
    city: str
    state: str

class Property(BaseModel):
    property_id: str
    name: str
    address: str
    city: str
    state: str

class City(BaseModel):
    city: str

class PropertyInDB(BaseModel):
    name: str
    address: str
    city: str
    state: str
    property_id: Optional[str] = None
