import os
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "economix_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import routes after app initialization to avoid circular imports
from routes import *
