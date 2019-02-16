from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login_page/login.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up/sign_up_page.html')
