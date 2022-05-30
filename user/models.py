import re
from flask import Flask, jsonify, request, redirect, url_for
import uuid

from passlib.hash import pbkdf2_sha256
from pymongo import MongoClient

# database connection
conn = MongoClient(
    "mongodb+srv://hmzakhan12:Hamza1243@cluster0.stcbu.mongodb.net/PetFinder?retryWrites=true&w=majority")

db = conn.PetFinder
UserDb = db.Users


class User:

    def startSession(self, user):
        import app
        del user['password']
        app.session['logged_in'] = True
        app.session['user'] = user

        return jsonify(user), 200

    def signup(self):

        # creating the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "location": request.form.get('location'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # encrypting the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # checking if the email address is already available

        if UserDb.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400

        if UserDb.insert_one(user):
            return self.startSession(user)

        return jsonify({"error": "Signup Failed"}), 400

    def signOut(self):

        import app
        app.session.clear()
        return redirect('/')

    def login(self):

        user = db.Users.find_one({"email": request.form.get('L_email')})

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.startSession(user)

        return jsonify({"error": "invalid details"}), 401
