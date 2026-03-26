from extension.db_conncetions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # Phone numbers should ALWAYS be strings, not integers, to keep the '+' sign and leading zeros!
    phone = db.Column(db.String(20), nullable=True) 
    
    # Date of Birth (Stored as a Date object or string like "YYYY-MM-DD")
    dob = db.Column(db.Date, nullable=True) 
    
    # Address can be long, so we use db.Text instead of db.String
    address = db.Column(db.Text, nullable=True)
    
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())