from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '9fa7c47531578ee3fef19c190c5c68e9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.db'

db = SQLAlchemy(app)

from flaskschedule import routes
