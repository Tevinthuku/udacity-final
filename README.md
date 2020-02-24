### Final Capstone Project

A flask app that enables Producers & directors to create movies and actors and also update and view them

### How to run this

1. Install dependencies `pip install -r requirements.txt`
2. Use the .env.sample as a template for setting up your .env file, I will have provided this in the submission notes though for an easier setup
3. Run `source .env`
4. Run `python api.py`
5. Run tests via `python test_api.py`

### How to login

Use the link below to login to the application

https://dev--rpzxv4r.auth0.com/authorize?audience=http://localhost:8080/&response_type=token&client_id=D2q1JWF7fyutvm5MuE6EYR6mbHnPy5jQ&redirect_uri=http://localhost:5000/login-results

### Production Link

https://udacity-tev-final.herokuapp.com/

### Endpoints & Roles

#### Casting Assistant

1. Can view actors and movies

```
GET /actors -> Get all actors
GET /movies -> Get all movies
```

#### Casting Director

1. All permissions a Casting Assistant has and…
2. Add or delete an actor from the database

```
POST /actors {name, bio} -> Create a new actor
DELETE /actors/<actor_id> -> Delete specific actor
```

3. Modify actors or movies

```
PATCH /actors/<actor_id> {name, bio} -> Update an actor
PATCH /movies/<movie_id> {title, description, agerestriction} -> Update a movie
```

#### Executive Producer

1. All permissions a Casting Director has and…
2. Add or delete a movie from the database

```
POST /movies/ {title, description, agerestriction} -> CREATE a movie
DELETE /movies/<movie_id> -> Delete a movie

```
