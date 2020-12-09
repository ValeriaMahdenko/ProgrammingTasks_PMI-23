from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_URI
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


