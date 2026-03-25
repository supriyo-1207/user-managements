from flask import Blueprint, request, jsonify
from DataBase.db_conncetions import db
from models.user_model import User

user=Blueprint('user', __name__)


@user.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name=data['name']
    email=data['email']
    password=data['password']

    if not name or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400
    
    # Check if email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already exists'}), 400

    # Save user data to the database
    try:
        # Step 1: Create the Python object
        new_user = User(name=name, email=email, password=password)

        # Step 2: Add to the database waiting room
        db.session.add(new_user)

        # Step 3: Commit permanently to MySQL
        db.session.commit()

        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    