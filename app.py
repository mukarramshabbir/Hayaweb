# app/main.py
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configure upload folder
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'app', 'uploads')

# Ensure the upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/advertisement')
def advertisement():
    return render_template('advertisment.html')

@app.route('/submit-account', methods=['POST'])
def submit_account():
    name = request.form.get('name')
    email = request.form.get('email')
    print(f"Received account submission: Name = {name}, Email = {email}")
    return redirect(url_for('index'))

@app.route('/submit-restaurant', methods=['POST'])
def submit_restaurant():
    restaurant_name = request.form.get('restaurantName')
    restaurant_image = request.files.get('restaurantImage')
    meal_images = request.files.getlist('mealImages')
    
    print(f"Restaurant Name: {restaurant_name}")
    
    # Save restaurant image
    if restaurant_image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], restaurant_image.filename)
        restaurant_image.save(image_path)
        print(f"Restaurant Image saved to: {image_path}")
    
    # Save meal images
    for meal_image in meal_images:
        if meal_image:
            meal_image_path = os.path.join(app.config['UPLOAD_FOLDER'], meal_image.filename)
            meal_image.save(meal_image_path)
            print(f"Meal Image saved to: {meal_image_path}")
    
    return redirect(url_for('index'))

