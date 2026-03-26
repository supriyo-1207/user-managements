from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import SQLALCHEMY_DATABASE_URI
from extension.db_conncetions import db
from routes.user_routes import user_blueprint
from extension.bcrypt import bcrypt
from extension.migrate import migrate

app = Flask(__name__)

# connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)     

# create the database tables
with app.app_context():
    db.create_all()

# initialize bcrypt
bcrypt.init_app(app)

# initialize migrate
migrate.init_app(app, db)
# register blueprints
app.register_blueprint(user_blueprint)



if __name__ == "__main__":
    app.run(debug=True)