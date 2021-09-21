Capstone Project
This project is created for complete Full Stack Web Developer Nanodegree Program.

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. 

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### Roles
Casting Assistant
   Can view actors, movies and movies_actors
   Token= eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InFOT19OYzZ4UkZWVW9UVzhfaVhCeiJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lZm5zZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0MjU1MDg0NDY3MmMwMDY5NGJlYTlmIiwiYXVkIjoiaW1hZ2UiLCJpYXQiOjE2MzIxOTY0OTMsImV4cCI6MTYzMjI4Mjg5MiwiYXpwIjoicGNNeW5sUFJ6YXp6WmtxWXlxa1RQTm9Xd2RhelZ2OVQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllc19hY3RvcnMiXX0.bc11J0i8IqbVAQV9Kre9rLUjQaxRIBku3JZ9Ao6tmY_pBoG5Y4Wa0P7rRHo2ddQFTIK83w6Czaaa5vk7FUdOOE_0QbVfRPpWZO58vB2-kGSK34Dowb6j76WAVz3Y4INN8WWfHYiYOQ4q8-Y-MudBwchq-iQc7Wha2Si89G4UVZ4xasW8Dug3kX8nF5a0dl31YmCgDohwagdxBtg9TWFwdZc4vQi5iOOEkohYa9U3koIYKaZkQAXhv24SkdDf2y88IzVo7xTzdmeQejayRgal3yUEFW_4qaV5mdToeh_TUzKgEIhdBECW2aE6OVz8Tse-DcpnBJvnCdzDpz5gnpscRw

Executive Producer
   All permissions for get, delete, patch and create
   Token= eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InFOT19OYzZ4UkZWVW9UVzhfaVhCeiJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lZm5zZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0MjU1MDg0NDY3MmMwMDY5NGJlYTlmIiwiYXVkIjoiaW1hZ2UiLCJpYXQiOjE2MzIxOTY2MjYsImV4cCI6MTYzMjI4MzAyNSwiYXpwIjoicGNNeW5sUFJ6YXp6WmtxWXlxa1RQTm9Xd2RhelZ2OVQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTptb3ZpZXNfYWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzX2FjdG9ycyIsInBhdGNoOmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJwb3N0Om1vdmllc19hY3RvcnMiXX0.KLvJ-c8W4QKvovJPsOklsYktC0A8u9tGOHOV5wbo9oy3T94fNO-mlnnO-W9AaFnr1HbgO5IA-huxlUZq0SATtaiFiLsqP_HWnH-AyRjWcbXGU_LBGzeevIrBmY50DIsgq9PRi5gdjbGRvMFeobs0nllGZmbigOj8V-HwhB4ylLOwewTbHUIREtDA6NNU_sytWCUIU7qkRcoT2W-zoAjjiPs2XSmLyhqlHh5uKYulP6JFe8wmB_JP1dr540yghRbUXvVb9dQpEGKYXoHNhJYxKWAy0pZGUKWXo99dReQf6uzukJBRQudZEc6duTPXWp2H6fKo_Lzr4iVb1rH97TozWA

### Endpoints
GET '/movies'
GET '/actors'
GET '/movies_actors'
POST '/movies'
POST '/actors'
POST '/movies_actors'
PATCH '/actor/<int:id>'
DELETE '/movies_actors/<int:movie_id>/<int:actor_id>'
```

GET '/movies'
```
- Fetches a dictionary of movies in which the keys are the ids and the values are title and release date
- Request Arguments: None
- Returns: An object with a single key, movies
- `curl http://127.0.0.1:5000/movies`
```

GET '/actors'
```
- Fetches a dictionary of actors in which the keys are the ids and the values are name, age and gender
- Request Arguments: None
- Returns: An object with a single key, actors
- `curl http://127.0.0.1:5000/actors`
```

GET '/movies_actors'
```
- Fetches a dictionary of movies_actors in which the keys are the ids to movies and actors
- Request Arguments: None
- Returns: An object with a single key, movies_actors
- `curl http://127.0.0.1:5000/movies_actors`
```


POST '/movies'
```
- General:
   - Creates a new movie. Returns the id of the created question, success value, and movies list.

- `curl -d '{"title":"Son como ninos", "release_date":"2015-02-21T21:30:00.000Z"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/movies`

```

POST '/actors'
```
- General:
   - Creates a new actor. Returns the id of the created question, success value, and actors list.

- `curl -d '{"name":"Juan Pablo Gonzalez", "age":22, "gender":"M"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/actors`

```

POST '/movies_actors'
```
- General:
   - Creates a new movies_actors. Returns the id of the created question, success value, and movies_actors list.

- `curl -d '{"movie_id":2, "actor_id":2}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/movies_actors`

```

PATCH '/actors/<int:id>'
```
- General:
   - Update a actors that already existed. 
   - Request Arguments: actor_id 

- `curl -d '{"name":"Camila Salazar", "gender":"F"}' -H "Content-Type: application/json" -X PATCH http://127.0.0.1:5000/actors/1`
```

DELETE '/movies_actors/<int:movie_id>/<int:actor_id>'
```
- DELETE a movies_actors by movie_id and actor_id
- Request Arguments: movie_id and actor_id
- Returns: Returns success value
- `curl -X DELETE http://127.0.0.1:5000/movies_actors/1/1`
```