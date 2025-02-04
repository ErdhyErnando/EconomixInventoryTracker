from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, login_manager, db
from models import User, Product, sample_products
import uuid

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', products=Product.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))

        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = str(uuid.uuid4())
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return render_template('register.html')

        user = User(id=user_id, username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('dashboard'))

    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/product/<int:product_id>')
@login_required
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/product/new', methods=['GET', 'POST'])
@login_required
def new_product():
    if request.method == 'POST':
        product = Product(
            name=request.form.get('name'),
            description=request.form.get('description'),
            quantity=int(request.form.get('quantity')),
            price=float(request.form.get('price')),
            image_url=request.form.get('image_url')
        )
        db.session.add(product)
        db.session.commit()
        flash('Product created successfully')
        return redirect(url_for('dashboard'))
    return render_template('product_form.html')

@app.route('/product/<int:product_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.quantity = int(request.form.get('quantity'))
        product.price = float(request.form.get('price'))
        product.image_url = request.form.get('image_url')
        db.session.commit()
        flash('Product updated successfully')
        return redirect(url_for('product_detail', product_id=product_id))

    return render_template('product_form.html', product=product)

@app.route('/product/<int:product_id>/delete', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully')
    return redirect(url_for('dashboard'))

def init_db():
    """Initialize the database with sample data."""
    if not Product.query.first():
        for product_data in sample_products:
            product = Product(**product_data)
            db.session.add(product)
        db.session.commit()