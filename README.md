# Property Management API

## Overview
This is a FastAPI-based web application for property management. It provides a set of APIs to perform operations related to properties such as creating new properties, fetching property details, updating property information, and more.

## Technologies Used
- FastAPI
- MongoDB

## Setup
1. **Clone the Repository:**
   ```sh
   git clone <repository_url>
   cd property-management-api
   ```

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Start MongoDB:**
   Ensure that MongoDB is running on your system. You can start MongoDB with the following command:
   ```sh
   mongod
   ```

4. **Run the FastAPI Server:**
   ```sh
   uvicorn main:app --reload
   ```

5. **Access the API Documentation:**
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by Swagger UI.

## API Endpoints

### 1. Create New Property
- **Endpoint:** `/property/create_new_property`
- **Method:** POST
- **Input:** Property name, address, city, and state.
- **Output:** List of properties with all details.

### 2. Fetch Property Details
- **Endpoint:** `/property/fetch_property_details`
- **Method:** GET
- **Input:** City name.
- **Output:** List of all properties that belong to the specified city.

### 3. Update Property Details
- **Endpoint:** `/property/update_property_details`
- **Method:** PUT
- **Input:** Property ID, property name, address, city, state.
- **Output:** Same as the `create_new_property` API with updated information.

### Additional APIs
- **Find Cities by State:**
  - **Endpoint:** `/property/find_cities_by_state`
  - **Method:** GET
  - **Input:** State ID or state name.
  - **Output:** All city names that belong to the specified state.

- **Find Similar Properties:**
  - **Endpoint:** `/property/find_similar_properties`
  - **Method:** GET
  - **Input:** Property ID.
  - **Output:** List of all properties that belong to the same city as the specified property ID.

## Testing
You can test the APIs using the interactive documentation available at `http://127.0.0.1:8000/docs`. Use tools like `curl`, Postman, or the interactive API documentation to make requests and check responses.
 
