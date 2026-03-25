from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import SQLALCHEMY_DATABASE_URI
from DataBase.db_conncetions import db
from routes.user_routes import user
from flask_bcrypt import Bcrypt


app = Flask(__name__)

# connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

# initialize bcrypt
bcrypt = Bcrypt(app)


# register blueprints
app.register_blueprint(user)



if __name__ == "__main__":
    app.run(debug=True)