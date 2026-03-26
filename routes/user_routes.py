from flask import Blueprint, request, jsonify
from extension.db_conncetions import db
from models.user_model import User
from extension.bcrypt import bcrypt


user_blueprint=Blueprint('user_blueprint', __name__)


@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name=data['name']
    email=data['email']
    password=str(data['password'])

    if not name or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400
    
    # Check if email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already exists'}), 400
    
    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Save user data to the database
    try:
        # Step 1: Create the Python object
        new_user = User(name=name, email=email, password=hashed_password)

        # Step 2: Add to the database waiting room
        db.session.add(new_user)

        # Step 3: Commit permanently to MySQL
        db.session.commit()

        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@user_blueprint.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    email=data['email']
    password=str(data['password'])

    # Check if email and password are provided
    if not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400
    
    # check if user exists
    user=User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    # check if password is correct
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid password'}), 401
    
    # login successful
    return jsonify({'message': 'Login successful'}), 200
    