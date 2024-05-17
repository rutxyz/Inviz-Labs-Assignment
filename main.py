from fastapi import FastAPI
from routes import router as property_router

app = FastAPI()

app.include_router(property_router, prefix="/property")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Property Management API"}
