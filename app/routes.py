from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    username = request.form['username']
    password = request.form['pass']
    remember_me = request.form['remember-me']
    print(username, password, remember_me)
    return render_template('login.html')

@app.route('/sign_up', methods=['POST'])
def sign_up():
    return render_template('sign_up.html')

@app.route('/about')
def about():
    return render_template('about.html')
