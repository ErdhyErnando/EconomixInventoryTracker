# Economix Inventory Management System

A Flask-based inventory management system for powdered drinks with user authentication and product tracking capabilities.

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Required Packages
```
flask==3.0.0
flask-login==0.6.3
flask-sqlalchemy==3.1.1
flask-wtf==1.2.1
email-validator==2.1.0
werkzeug==3.0.1
```

## Local Setup Instructions

1. Clone the repository to your local machine:
```bash
git clone <repository-url>
cd economix-inventory
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up the environment variables (optional):
```bash
# On Windows
set FLASK_SECRET_KEY=your_secret_key_here

# On macOS/Linux
export FLASK_SECRET_KEY=your_secret_key_here
```

5. Run the application:
```bash
python main.py
```

6. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

## Project Structure
```
economix-inventory/
├── static/
│   ├── css/
│   │   └── custom.css
│   └── js/
│       ├── charts.js
│       └── main.js
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── product_detail.html
│   ├── product_form.html
│   └── register.html
├── app.py
├── main.py
├── models.py
└── routes.py
```

## Features
- User Authentication (Register/Login)
- Product Management (CRUD operations)
- Responsive Design
- Product Analytics with Charts
- SQLite Database

## Database
The application uses SQLite as the database, which will be automatically created as `economix.db` in the instance folder when you first run the application.

## First Time Setup
1. When you first run the application, the database will be automatically created with some sample products.
2. Register a new user account through the registration page.
3. Log in with your credentials to access the dashboard.

## Development
- The application runs in debug mode by default
- Flask's development server will automatically reload when you make changes to the code
- SQLite database file is created in the `instance` folder

## Note
This is a development setup and should not be used in production without proper security measures and configurations.
