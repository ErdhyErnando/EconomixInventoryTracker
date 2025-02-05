from app import app, db
from models import *

with app.app_context():
    db.drop_all()  # This will drop all existing tables
    db.create_all()  # This will create new tables with updated schema
    
    # You can add some initial data here if needed
    print("Database initialized successfully!")