from flask import render_template, request, url_for, redirect
from app import app
from app import app, db
from flask_login import current_user, login_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])

@app.route('/login', methods=["GET"])
def display_login():
    return render_template('login.html')



@app.route('/login_handle', methods=["POST","GET"])


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
                login_user()
                print('attempted to log in user')
            else:
                return render_template('login.html', error="Invalid password or username.")
    return redirect(url_for('index'))

@app.route('/sign_up', methods=['GET', 'POST'])
def display_sign_up():
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

        if not password == password2:
            return render_template('sign_up.html', error="Passwords do not match.")

        if not -1 in [username, email, password, password2]:
            # check if user exsits
            user = User.query.filter_by(username=username).first()

            if not user:    # if user does not exist, then create
                # this path leads to success
                u = User(username=username, email=email)
                u.set_password(password)
                db.session.add(u)
                db.session.commit()
                return redirect(url_for('index'))

            else:   # else, say it already exists
                return render_template('sign_up.html', error="Username already taken.")
        else:
            return render_template('sign_up.html', error="Please complete the form.")

@app.route('/about')
def about():
    return render_template('about.html')
