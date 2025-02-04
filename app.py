import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "economix_secret_key"

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///economix.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import routes after app initialization to avoid circular imports
from routes import *
from routes import init_db

# Create database tables and initialize with sample data
with app.app_context():
    db.create_all()
    init_db()