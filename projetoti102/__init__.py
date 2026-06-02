from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ti102.db'
database = SQLAlchemy(app)

from projetoti102 import routes, models
