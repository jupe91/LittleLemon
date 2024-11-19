 API paths

for all menu items
GET http://127.0.0.1:8000/api/menu-items/

### API Endpoints:

1. **Get All Menu Items**  
   **Path**: `GET /api/menu-items/`  
   **Description**: Retrieves a list of all menu items in the restaurant.

GET http://127.0.0.1:8000/api/menu-items/

2. **Get a Single Menu Item by ID**  
**Path**: `GET /api/menu-items/<id>/`  
**Description**: Retrieves the details of a specific menu item by its ID.

GET http://127.0.0.1:8000/api/menu-items/1/

3. **Create a New Menu Item**  
**Path**: `POST /api/menu-items/`  
**Description**: Adds a new menu item. You need to send the `dish`, `price`, and `inventory` fields.

POST http://127.0.0.1:8000/api/menu-items

4. **Update an Existing Menu Item**  
**Path**: `PUT /api/menu-items/<id>/`  
**Description**: Updates the details of a specific menu item. You must provide the item's ID and fields you want to update.

PUT http://127.0.0.1:8000/api/menu-items/1


5. **Delete a Menu Item**  
**Path**: `DELETE /api/menu-items/<id>/`  
**Description**: Deletes a specific menu item by its ID.

DELETE http://127.0.0.1:8000/api/menu-items/1


auth_token": "b29b89d88aa48ecfed180b10b5c5e72f22f684b3"

