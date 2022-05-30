from functools import wraps

from flask import Flask, render_template, session, redirect, request
from user.models import User
from Animals.AnimalModel import Animals

import os
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "HamzaKhan1243"


@app.route('/user/signup/', methods=['POST'])
def signup():
    user = User()
    return user.signup()


# Decorator func
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


@app.route('/')
def home():
    if 'logged_in' in session:
        return redirect('/dashboard/')
    return render_template('A_landing.html')


@app.route('/signup')
def UserSignUp():
    return render_template('signup.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/user/signout')
def signout():
    return User().signOut()


@app.route('/login')
def loginPage():
    if 'logged_in' in session:
        return redirect('/dashboard/')
    return render_template('login.html')


@app.route('/user/login/', methods=['POST'])
def login():
    return User().login()


@app.route('/info')
@login_required
def Info():
    return render_template('info.html')


@app.route('/post')
def post():
    return render_template('LostAndFound.html')


@app.route('/post/animal', methods=['POST'])
def FoundAnimal():
    return Animals().Post()


if __name__ == "__main__":
    app.run(debug=True)
