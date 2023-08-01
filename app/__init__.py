from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/storage.db'
app.config['DEBUG'] = True
database = SQLAlchemy(app)

from app.controllers import routes
