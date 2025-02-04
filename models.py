from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# In-memory storage
users = {}
products = {}
stock_history = {}

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

class Product:
    def __init__(self, id, name, description, quantity, price, image_url):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.image_url = image_url
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

# Sample product data
sample_products = [
    {
        "id": 1,
        "name": "Berry Blast Mix",
        "description": "A refreshing berry-flavored drink mix",
        "quantity": 100,
        "price": 9.99,
        "image_url": "https://images.unsplash.com/photo-1496318447583-f524534e9ce1"
    },
    {
        "id": 2,
        "name": "Tropical Paradise",
        "description": "Exotic tropical fruit blend",
        "quantity": 75,
        "price": 11.99,
        "image_url": "https://images.unsplash.com/photo-1470337458703-46ad1756a187"
    }
]

# Initialize sample data
for product_data in sample_products:
    product = Product(**product_data)
    products[product.id] = product
