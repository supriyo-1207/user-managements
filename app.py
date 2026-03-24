from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import SQLALCHEMY_DATABASE_URI
from DataBase.db_conncetions import db

app = Flask(__name__)

# connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)