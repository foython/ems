# Employer Management System API

A Django REST Framework-based API for managing employers with custom user authentication using JWT tokens.

## Prerequisites

- Python 3.7+
- pip

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/foython/ems.git
   cd ems
2. Create and activate a virtual environment
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt
4. Apply migrations
   python manage.py makemigrations
   python manage.py migrate


Authentication Endpoints
Sign Up

http
POST /api/auth/signup/
Body (JSON):
{
    "email": "user@gmail.com",
    "password": "123456",
    "first_name": "Sajid",
    "last_name": "Hasan"
   }
   
Login (Get JWT Tokens)

http
POST /api/auth/login/
Body (JSON):
{
    "email": "user@example.com",
    "password": "securepassword123"
}
Response includes:
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
Get Profile

http
GET /api/auth/profile/
Headers:
Authorization: Bearer <access_token>
Employer Endpoints (Require JWT)
Create Employer

http
POST /api/employers/
Headers:
Authorization: Bearer <access_token>
Body (JSON):
{
    "company_name": "Tech Corp",
    "contact_person_name": "John Doe",
    "email": "info@techcorp.com",
    "phone_number": "+1234567890",
    "address": "123 Main St, City"
}
List Employers

http
GET /api/employers/list/
Headers:
Authorization: Bearer <access_token>
Retrieve/Update/Delete Employer

http
GET/PUT/DELETE /api/employers/<id>/
Headers:
Authorization: Bearer <access_token>
   

