from flask import Flask, request, url_for, jsonify, redirect

import os
import uuid
from pymongo import MongoClient
from werkzeug.utils import secure_filename

conn = MongoClient(
    "mongodb+srv://hmzakhan12:Hamza1243@cluster0.stcbu.mongodb.net/PetFinder?retryWrites=true&w=majority")
db = conn.PetFinder
AnimalDb = db.Animals

AllowedExtension = set(['png', 'jpg', 'jpeg', 'gif'])


class Animals:

    def Post(self):

        import app
        if request.method == "POST":

            if 'image' in request.files:

                f = request.files['image']
                print(f)


            AnimalDb.insert_one({
                "_id": uuid.uuid4().hex,
                "user": app.session['user']['_id'],
                "type": request.form.get('type'),
                "location": request.form.get('petLocation'),
                "picture": "f"
            })
        else:

            return jsonify({"error": "wrong file"}), 400
        jsonify("success!"), 200
        return redirect('/dashboard')