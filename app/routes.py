from flask import render_template, request, url_for, redirect
from app import app, db
from flask_login import current_user, login_user
from app.models import User
from datetime import datetime
import base64, os


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/photo_handle', methods=["POST"])
def photo_handle():
    #data = request.form.get("data", True)
    try:
        print('photo handling')
        null, data = request.form['data'].split(',', 1)
        with open('log.txt', 'w') as fuckbase64:
            fuckbase64.write(data)
            fuckbase64.write('\n')
        with open("imag.png", "wb") as fout:
            fout.write(base64.b64decode(data))
        data = request.form['uuaa']
        print("Request Received")
        print(os.chdir('../images_backend'))
        print('dir changed', os.getcwd())
        fo = open("img.png", "wb")
        print("img saved")
        data = base64.b64decode(data)
        fo.write(data)
        print('img written')
        fo.close()
    except:
        pass
    return "0"



@app.route('/login', methods=["GET"])
def display_login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('login.html')



@app.route('/login_handle', methods=["GET", "POST"])
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
            if user and user.check_password(password):
                print("User logged in, ", user)
                login_user(user)
            else:
                return render_template('login.html', error="Invalid password or username.")
    return redirect(url_for('index'))

@app.route('/sign_up', methods=['GET', 'POST'])
def display_sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('sign_up.html')

@app.route('/sign_up_handle', methods=['GET', 'POST'])
def sign_up():
    global db
    username, password, email, password2 = -1, -1, -1, -1
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

        # 'validate' email
        if not all(s in email for s in ['@', '.']):
            return render_template('sign_up.html', error="Invalid email.")

        if not password == password2:
            return render_template('sign_up.html', error="Passwords do not match.")

        if not -1 in [username, email, password, password2]:
            # check if user exsits
            user = User.query.filter_by(username=username).first()

            if not user:    # if user does not exist, then create
                # this path leads to success

                if User.query.filter_by(email=email).first():   # if email already exists...
                    return render_template('sign_up.html', error="There is already an account with that email.")

                u = User(username=username, email=email)
                u.set_password(password)
                db.session.add(u)
                db.session.commit()
                return redirect(url_for('index'))

                return render_template('sign_up.html', error="Username already taken.")
        else:
            return render_template('sign_up.html', error="Please complete the form.")

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/base')
def base():
    return render_template('base.html')
