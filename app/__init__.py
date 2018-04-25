import os
from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from subprocess import call

UPLOAD_FOLDER = '/UPLOAD_FOLDER'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://mzihlvlmbzdhkb:c5409d82259f28ff87d5fc8e411af52c6d68d3083ad9d74853a3f1ebe002db99@ec2-54-163-246-193.compute-1.amazonaws.com:5432/d8qhck545uolku'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views