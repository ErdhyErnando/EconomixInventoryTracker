from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, login_manager, db
from models import User, Product, sample_products, StockHistory, PriceHistory
import uuid
from datetime import datetime, timedelta

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

    # Get history data for last 6 months
    six_months_ago = datetime.utcnow() - timedelta(days=180)
    
    stock_history = (StockHistory.query
                     .filter(StockHistory.product_id == product_id)
                     .filter(StockHistory.date >= six_months_ago)
                     .order_by(StockHistory.date)
                     .all())
    
    price_history = (PriceHistory.query
                     .filter(PriceHistory.product_id == product_id)
                     .filter(PriceHistory.date >= six_months_ago)
                     .order_by(PriceHistory.date)
                     .all())
    
    history_data = {
        'dates': [h.date.strftime('%Y-%m-%d') for h in stock_history],
        'stock_data': [h.quantity for h in stock_history],
        'price_data': [h.price for h in price_history]
    }
    
    print("Debug - History Data:", history_data)  # Add this debug line
    
    return render_template('product_detail.html', 
                         product=product,
                         history_data=history_data)



@app.route('/product/new', methods=['GET', 'POST'])
@login_required
def new_product():
    if request.method == 'POST':
        quantity = int(request.form.get('quantity'))
        price = float(request.form.get('price'))
        
        product = Product(
            name=request.form.get('name'),
            description=request.form.get('description'),
            quantity=quantity,
            price=price,
            image_url=request.form.get('image_url')
        )
        db.session.add(product)
        db.session.flush()  # This gets us the product.id
        
        # Create initial history records
        stock_history = StockHistory(
            product_id=product.id,
            quantity=quantity
        )
        price_history = PriceHistory(
            product_id=product.id,
            price=price
        )
        
        db.session.add(stock_history)
        db.session.add(price_history)
        
        db.session.commit()
        flash('Product created successfully')
        return redirect(url_for('dashboard'))
    return render_template('product_form.html')


@app.route('/product/<int:product_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        new_quantity = int(request.form.get('quantity'))
        new_price = float(request.form.get('price'))
    
        # track stock changes
        if new_quantity != product.quantity:
            stock_history = StockHistory(
                product_id=product_id,
                quantity=new_quantity
            ) 
            db.session.add(stock_history)
        
        # track price changes
        if new_price != product.price:
            price_history = PriceHistory(
                product_id=product_id,
                price=new_price
            )
            db.session.add(price_history)
        
        # update product details
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.quantity = new_quantity
        product.price = new_price
        product.image_url = request.form.get('image_url')

        db.session.commit()
        flash('Product updated successfully')
        return redirect(url_for('product_detail', product_id=product_id))

    return render_template('product_form.html', product=product)



@app.route('/product/<int:product_id>/delete', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)

    PriceHistory.query.filter_by(product_id=product_id).delete()
    StockHistory.query.filter_by(product_id=product_id).delete()
    
    # Delete the product
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