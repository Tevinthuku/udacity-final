import os
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

from database.models import setup_db, db_drop_and_create_all, Movie, Actor

app = Flask(__name__)
setup_db(app)
CORS(app)

# db_drop_and_create_all()


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

# Actors endpoints
@app.route("/actors")
def get_actors():
    all_actors = Actor.query.all()
    return jsonify({
        "success": True,
        "actors": [actor.repr() for actor in all_actors]
    }), 200


@app.route("/actors", methods=["POST"])
def post_actor():
    req = request.get_json()

    try:
        name = req["name"]
        bio = req["bio"]
        actor = Actor(name=name, bio=bio)
        actor.insert()
        return jsonify({
            "success": True,
            "actor": actor.repr()
        })
    except:
        abort(400)


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
def edit_actor(actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actor is None:
        abort(404)
    actor.name = request.json.get('name') or actor.name
    actor.bio = request.json.get('bio') or actor.bio
    actor.update()
    return jsonify({
        "success": True,
        "actor": [actor.repr()]
    }), 200


@app.route('/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actor is None:
        abort(404)
    actor.delete()
    return jsonify({
        "success": True,
        "delete": actor_id
    }), 200


# Movies endpoints
@app.route("/movies")
def get_movies():
    all_movies = Movie.query.all()
    return jsonify({
        "success": True,
        "movies": [movie.repr() for movie in all_movies]
    }), 200


@app.route("/movies", methods=["POST"])
def post_movie():
    req = request.get_json()
    try:
        title = req["title"]
        description = req["description"]
        agerestriction = req["agerestriction"]
        movie = Movie(title=title, description=description,
                      agerestriction=agerestriction)
        movie.insert()
        return jsonify({
            "success": True,
            "movie": movie.repr()
        }), 200
    except:
        abort(400)


@app.route('/movies/<int:movie_id>', methods=['PATCH'])
def edit_movie(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if movie is None:
        abort(404)
    movie.title = request.json.get('title') or movie.title
    movie.description = request.json.get('description') or movie.description
    movie.agerestriction = request.json.get(
        'agerestriction') or movie.agerestriction

    movie.update()
    return jsonify({
        "success": True,
        "actor": [movie.repr()]
    }), 200


@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if movie is None:
        abort(404)
    movie.delete()
    return jsonify({
        "success": True,
        "movie": movie_id
    }), 200


@app.errorhandler(400)
def badrequest(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource not found"
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
    }), 500