from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask_migrate import Migrate

from models import Movie_Actor, db_drop_and_create_all, setup_db, Movie, Actor, db
from auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
migrate = Migrate(app, db)
CORS(app)

'''
!! Running this funciton will delete and add demo data
'''
db_drop_and_create_all()

# ROUTES
'''
    GET /movie
    Return All movies
'''
@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_all_movies(payload):
    if request.method == "GET":
        moviesdb = Movie.query.all()

        if len(moviesdb) == 0:
            abort(404)

        movies = [movie.format() for movie in moviesdb]
          
        return jsonify({
            'success': True,
            'movies': movies
          }), 200


'''
    GET /actors
    Return All actors
'''
@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_all_actors(payload):
    if request.method == "GET":
        actorsdb = Actor.query.all()

        if len(actorsdb) == 0:
            abort(404)

        actors = [actor.format() for actor in actorsdb]
          
        return jsonify({
            'success': True,
            'actor': actors
          }), 200


'''
    GET /movie_actor
    Return All movies by actors
'''
@app.route('/movies_actors', methods=['GET'])
@requires_auth('get:movies_actors')
def get_all_movies_actors(payload):
    if request.method == "GET":
        movies_actorsdb = Movie_Actor.query.all()

        if len(movies_actorsdb) == 0:
            abort(404)

        movies_actors = [movie_actor.format() for movie_actor in movies_actorsdb]
          
        return jsonify({
            'success': True,
            'movies_actors': movies_actors
          }), 200

'''
@TODO implement endpoint
    POST /movies
'''
@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def create_movie(payload):
    if request.method == "POST":
        body = request.get_json()

        try:
            movies_title = body.get('title')
            movies_release_date = body.get('release_date')

            movie = Movie(title=movies_title, release_date=movies_release_date)
            movie.insert()

            movies = [movie.format()]

            return jsonify({
                'success': True,
                'movies': movies
                }), 200

        except:
            abort(422)

'''
@TODO implement endpoint
    POST /actors
'''
@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def create_actors(payload):
    if request.method == "POST":
        body = request.get_json()

        try:
            actors_name = body.get('name')
            actors_age = body.get('age')
            actors_gender = body.get('gender')

            actor = Actor(name=actors_name, age=actors_age, gender=actors_gender)
            actor.insert()

            actors = [actor.format()]

            return jsonify({
                'success': True,
                'actor': actors
                }), 200

        except:
            abort(422)


'''
@TODO implement endpoint
    POST /movies_actors
'''
@app.route('/movies_actors', methods=['POST'])
@requires_auth('post:movies_actors')
def create_movies_actors(payload):
    if request.method == "POST":
        body = request.get_json()

        try:
            movies_id = body.get('movie_id')
            actors_id = body.get('actor_id')

            movie_actor = Movie_Actor(movie_id=movies_id, actor_id=actors_id)
            movie_actor.insert()

            movies_actors = [movie_actor.format()]

            return jsonify({
                'success': True,
                'movies_actors': movies_actors
                }), 200

        except:
            abort(422)

'''
@TODO implement endpoint
    PATCH /actors/<id>
    returns status code 200 and json {"success": True, "actors": actors} where actors an array containing only the updated actor
        or appropriate status code indicating reason for failure
'''
@app.route('/actors/<int:id>', methods=['PATCH'])
@requires_auth('patch:actors') 
def update_actor(payload, id):
    if request.method == "PATCH":
        body = request.get_json()

        actor = Actor.query.filter(Actor.id==id).one_or_none()

        if not actor:
            abort(404)

        try:
            actors_name = body.get('name', None)
            actors_age = body.get('age', None)
            actors_gender = body.get('gender', None)

            if actors_name != None:
                actor.name = actors_name
            
            if actors_age != None:
                actor.age = actors_age

            if actors_gender != None:
                actor.gender = actors_gender

            actor.update()

            actors = [actor.format()]

            return jsonify({
                'success': True,
                'actors': actors
                }), 200
        except:
            abort(422)


'''
@TODO implement endpoint
    DELETE /actors/<movies_id>/<actors_id>
    returns status code 200 and json {"success": True}
'''
@app.route('/movies_actors/<int:movies_id>/<int:actors_id>', methods=['DELETE'])
@requires_auth('delete:movies_actors')
def delete_movies_actors(payload,movies_id, actors_id):
    if request.method == "DELETE":
        
        try:
            movies_actors = Movie_Actor.query.filter(Movie_Actor.actor_id==actors_id).filter(Movie_Actor.movie_id==movies_id).one_or_none()

            if movies_actors is None:
                abort(404)

            movies_actors.delete()

            return jsonify({
                'success': True
            }), 200

        except:
            abort(422)
        


# Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401

@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "forbidden"
    }), 403


@app.errorhandler(405)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
    }), 405

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 500

@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code