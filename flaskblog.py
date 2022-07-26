
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Post

app = Flask(__name__) # __name__ ist eine spezielle Variable in Python: der Name vom Modul. Wenn man es in Python direkt ablaufen lässt, dann gilt: __name__ = __main__
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # The database URI that should be used for the connection. /// for relative path, creates site.db in project folder
db = SQLAlchemy(app) # Erzeuge Instanz von SQLAlchemy

#Connect to Database and create database session
engine = create_engine('sqlite:///site.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/") # mit dem Slash ist die Stammwebseite gemeint aka Homepage
@app.route("/home") # zweite Route für den gleichen Inhalt
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") # mit dem Slash ist die Stammwebseite gemeint aka Homepage
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
