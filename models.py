from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    completion_date = db.Column('Completion Date', db.DateTime)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.String())
    github = db.Column('Github', db.String())
    screenshot = db.Column('Screenshot URL', db.String())