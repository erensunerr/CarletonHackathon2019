from flask import render_template, request, url_for, redirect
from app import app
from flask_login import current_user, login_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    username, password = -1, -1
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
    return redirect(url_for('index'))

@app.route('/sign_up', methods=['POST','GET'])
def sign_up():
    global db
    username, password, email, password2 = -1,-1,-1,-1
    if current_user.is_authenticated:
        return redirect(url_for('/index'))
    else:
        try:
            username = request.form['username']
            password = request.form['pass']
            password2 = request.form['repeat-pass']
            email = request.form['email']
        except:
            pass
        if username != -1 and password != -1 and email != -1 and password2 != -1 :
            user = User.query.filter_by(username=username).first()
            if not user:
                u = User(username=username, email=email)
                u.set_password(password)
                db.session.add(u)
                db.session.commit()
                return redirect(url_for('/index'))
            else:
                return render_template('sign_up.html', error="Username already taken.")
        else:
            return render_template('sign_up.html', error="Please complete the form.")

@app.route('/about')
def about():
    return render_template('about.html')
