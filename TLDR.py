from pickle import TRUE
import random
import re
from webbrowser import get
from click import argument
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv
from cgitb import html
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import *
load_dotenv() 

app = Flask(__name__)
'''
app.secret_key = os.getenv('secret_key')

app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

lm = LoginManager()
lm.login_view = 'auth.login'
lm.init_app(app)

this databse will keep track of all the users and will be used later for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80),  nullable = True)
    
    def __repr__(self):
        return '<Comments %r>' % self.username
    def __str__(self):
        return f'{self.username}'

#this databse will keep track of all the comments and be accessed later to display comments across sessions
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80),  nullable = True)
    summary_title = db.Column(db.String(100), nullable = True
    summary = db.Column(db.String(1000000), nullable = True)
    
    def __str__(self):
       return f'{self.username} {self.summary}'


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()
'''
@app.route('/')
def index():
    return render_template('main_page.html')

@app.route('/summerize_text', methods = ['POST'])
def summerize_text():
    form_data = request.form
    initial_text = form_data['initial_text']
    global summary_title; summary_title = form_data['summary_title']
    global summary; summary  = initial_text + " this will be summized"
    return redirect(url_for('summary_maker'))


@app.route('/summary')
def summary_maker():
    #will return the summary of the initial text 
    return render_template(
        'summary_page.html', 
        html_summary = summary
    )

@app.route('/view_summeries', methods = ['POST'])
def view_summeries():
    return redirect(url_for('your_summeries'))

@app.route('/your_summaries')
def your_summeries():
    return render_template(
        'your_summeries.html', 
        html_summary_title = summary_title 
             
        )

app.run()