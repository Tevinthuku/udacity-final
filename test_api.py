from flask import Flask
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api import app


db = SQLAlchemy()


class appDBTests(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        self.app = app
        self.client = self.app.test_client

        database_filename = "database.db"
        project_dir = os.path.dirname(os.path.abspath(__file__))
        database_path = "sqlite:///{}".format(
            os.path.join(project_dir, database_filename))
        self.app.config["SQLALCHEMY_DATABASE_URI"] = database_path
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.executiveProducerToken = os.getenv("EXECUTIVE_PRODUCER_TOKEN")
        self.castingDirectorToken = os.getenv("CASTING_DIRECTOR_TOKEN")
        self.castingAssistantToken = os.getenv("CASTING_ASSISTANT_TOKEN")
        # data
        self.new_movie = {
            "title": "New Movie",
            "description": "Describe the new movie",
            "agerestriction": 12
        }
        self.new_actor = {
            "name": "New Actor",
            "bio": "Lorem ipsum 24"
        }
        db.app = self.app
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        with self.app.app_context():
            db.drop_all()

    def get_movies(self, headers):
        return self.client().get('/movies', headers=headers)

    def get_actors(self, headers):
        return self.client().get("/actors", headers=headers)

    def create_movie(self, headers):
        return self.client().post('/movies', json=self.new_movie, headers=headers)

    def delete_movie(self, headers, id):
        return self.client().delete("/movies/{}".format(id), headers=headers)

    def create_actor(self, headers):
        return self.client().post("/actors", json=self.new_actor, headers=headers)

    def delete_actor(self, headers, actor_id):
        return self.client().delete("/actors/{}".format(actor_id), headers=headers)

    def modify_movie(self, headers, movie_id, new_content):
        return self.client().patch("/movies/{}".format(movie_id), headers=headers, json=new_content)

    def modify_actor(self, headers, actor_id, new_info):
        return self.client().patch("/actors/{}".format(actor_id), headers=headers, json=new_info)

    # Executive Producer tests

    def test_create_movie(self):
        res = self.create_movie({
            "authorization": self.executiveProducerToken
        })
        self.assertEqual(json.loads(res.data)["movie"]["title"], "New Movie")
        self.assertEqual(res.status_code, 200)

    def test_delete_movie(self):
        movie_created = self.create_movie({
            "authorization": self.executiveProducerToken
        })
        movie_id = json.loads(movie_created.data)["movie"]["id"]
        res = self.delete_movie({
            "authorization": self.executiveProducerToken
        }, movie_id)
        self.assertEqual(json.loads(res.data), {
                         "movie": movie_id, "success": True})
        self.assertEqual(res.status_code, 200)

    # Casting director
    def test_add_actor(self):
        res = self.create_actor({
            "authorization": self.castingDirectorToken})
        self.assertTrue(json.loads(res.data)["success"])
        self.assertEqual(res.status_code, 200)

    def test_delete_actor(self):
        actor_created = self.create_actor({
            "authorization": self.castingDirectorToken
        })

        actor_id = json.loads(actor_created.data)["actor"]["id"]

        res = self.delete_actor({
            "authorization": self.castingDirectorToken
        }, actor_id)
        self.assertEqual(json.loads(actor_created.data)
                         ["actor"]["name"], "New Actor")
        self.assertEqual(res.status_code, 200)

    def test_modify_movie(self):
        movie_created = self.create_movie({
            "authorization": self.executiveProducerToken
        })

        movie_id = json.loads(movie_created.data)["movie"]["id"]
        new_movie_title = "New Name of Movie"
        movie_modified = self.modify_movie({
            "authorization": self.castingDirectorToken
        }, movie_id, {
            "title": new_movie_title
        })
        self.assertEqual(movie_modified.status_code, 200)

        self.assertEqual(
            json.loads(movie_modified.data)["movie"]["title"],
            new_movie_title)

    def test_modify_actor(self):
        actor_created = self.create_actor({
            "authorization": self.castingDirectorToken})
        new_actor_name = "New Actor Name"
        actor_id = json.loads(actor_created.data)["actor"]["id"]
        res = self.modify_actor({
            "authorization": self.castingDirectorToken
        }, actor_id, {
            "name": new_actor_name
        })
        self.assertEqual(
            json.loads(res.data)["actor"]["name"],
            new_actor_name)

    # Casting Assistant

    def test_view_actors(self):
        res = self.get_actors({
            "authorization": self.castingAssistantToken
        })
        actors_length = len(json.loads(res.data)["actors"])
        self.create_actor({
            "authorization": self.castingDirectorToken})
        refetch_actors = self.get_actors({
            "authorization": self.castingAssistantToken
        })
        self.assertEqual(len(json.loads(refetch_actors.data)
                             ["actors"]), actors_length+1)

    def test_view_movies(self):
        res = self.get_movies({
            "authorization": self.castingAssistantToken
        })
        movies_length = len(json.loads(res.data)["movies"])
        self.create_movie({
            "authorization": self.executiveProducerToken})
        refetch_movies = self.get_movies({
            "authorization": self.castingAssistantToken
        })
        self.assertEqual(len(json.loads(refetch_movies.data)
                             ["movies"]), movies_length+1)

    # Errors

    def test_error_getting_movies_without_token(self):
        res = self.get_movies({})
        self.assertEqual(res.status_code, 401)

    def test_error_getting_actors_without_token(self):
        res = self.get_actors({})
        self.assertEqual(res.status_code, 401)

    def test_casting_director_attempt_to_create_movie(self):
        res = self.create_movie({
            "authorization": self.castingDirectorToken
        })

        self.assertEqual(res.status_code, 401)

    def test_casting_director_attempt_to_delete_movie(self):
        res = self.create_movie({
            "authorization": self.executiveProducerToken
        })
        id = json.loads(res.data)["movie"]["id"]
        delete_movie = self.delete_movie({
            "authorization": self.castingDirectorToken
        }, id)

        self.assertEqual(delete_movie.status_code, 401)

    def test_modify_non_existent_movie(self):
        movie_created = self.create_movie({
            "authorization": self.executiveProducerToken
        })
        movie_id = json.loads(movie_created.data)["movie"]["id"]
        new_movie_title = "New Name of Movie"
        non_existent_id = movie_id * movie_id
        movie_modified = self.modify_movie({
            "authorization": self.castingDirectorToken
        }, non_existent_id, {
            "title": new_movie_title
        })
        self.assertEqual(movie_modified.status_code, 404)

    def test_modify_non_existent_actor(self):
        movie_created = self.create_actor({
            "authorization": self.executiveProducerToken
        })
        actor_id = json.loads(movie_created.data)["actor"]["id"]
        new_actor_name = "New Name of Actor"
        non_existent_id = actor_id * actor_id
        movie_modified = self.modify_actor({
            "authorization": self.castingDirectorToken
        }, non_existent_id, {
            "name": new_actor_name
        })
        self.assertEqual(movie_modified.status_code, 404)


if __name__ == "__main__":
    unittest.main()
