import os
from flask import Flask
from flask_cors import CORS

from database.models import setup_db, db_drop_and_create_all, Movie

app = Flask(__name__)
setup_db(app)
CORS(app)

db_drop_and_create_all()


@app.route('/')
def get_greeting():
    greeting = "Hello"
    # movie = Movie(title="New Movie",
    #               description="Nice 1", agerestriction=12)

    # movie.insert()
    # print(movie)

    return greeting


@app.route('/coolkids')
def be_cool():
    return "Be cool, man, be coooool! You're almost a FSND grad!"
