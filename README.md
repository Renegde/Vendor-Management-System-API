This is a Vendor Management System API developed using Django and Django REST Framework. 
It allows you to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

Table of Contents
Getting Started
  Prerequisites
  Installation
API Endpoints
Token-based Authentication
Testing
Contributing
License

Getting Started
Prerequisites
  Python 3.x
  Django
  Django REST Framework
  Django REST Framework SimpleJWT


Installation
Clone the repository
git clone https://github.com/yourusername/vendor-management-api.git
cd vendor-management-api

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Run the development server:
python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/api/.

API Endpoints
Vendor Endpoints:

  POST /api/vendors/: Create a new vendor.
  GET /api/vendors/: List all vendors.
  GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
  PUT /api/vendors/{vendor_id}/: Update a vendor's details.
  DELETE /api/vendors/{vendor_id}/: Delete a vendor.
  GET /api/vendors/{vendor_id}/performance/: Retrieve a vendor's performance metrics.

Purchase Order Endpoints:
  POST /api/purchase_orders/: Create a purchase order.
  GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
  GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
  PUT /api/purchase_orders/{po_id}/: Update a purchase order.
  DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

Token-based Authentication
  To obtain tokens, make a POST request to /api/token/ with the user credentials.
  Include the access token in the Authorization header for authenticated requests.
  To refresh an expired token, make a POST request to /api/token/refresh/ with the refresh token.


  
