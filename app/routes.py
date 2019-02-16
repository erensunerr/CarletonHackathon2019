from flask import render_template, request
from app import app
from flask_login import current_user, login_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST","GET"])
def login():
    username, password = -1,-1
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        try:
            username = request.form['username']
            password = request.form['pass']
            remember_me = request.form['remember-me']
        except:
            pass
        if username != -1 and password != -1:
            user = User.query.filter_by(username=username).first()
            if not(user is None) or user.check_password(password):
                login_user()
            else:
                render_template('login.html', error="Invalid password or username.")
    return render_template('login.html')

@app.route('/sign_up', methods=['POST'])
def sign_up():
        username, password = -1,-1
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        else:
            try:
                username = request.form['username']
                password = request.form['pass']
                password2 = request.form['repeat-pass']
                email = request.form['email']
            except:
                pass
            if username != -1 and password != -1:
                user = User.query.filter_by(username=username).first()
                if not :
                    print('Invalid username or password')
        return render_template('login.html')
    return render_template('sign_up.html')

@app.route('/about')
def about():
    return render_template('about.html')
