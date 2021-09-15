Capstone Project 

- Postman test
- Endpoints
- Auth JWT

Endpoints
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