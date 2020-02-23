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
        self.executiveProducerToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EZEROVGsxTUVZeVJEUTVORVV4T1RKRFJFUTVOak00UXpneU1qa3pOakV6UkRWRFJrUkJRdyJ9.eyJpc3MiOiJodHRwczovL2Rldi0tcnB6eHY0ci5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTY3NzYxMjA0OTM1MTMzNzMwOTUiLCJhdWQiOlsiaHR0cDovL2xvY2FsaG9zdDo4MDgwLyIsImh0dHBzOi8vZGV2LS1ycHp4djRyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODI0NjU3NjEsImV4cCI6MTU4MjU1MjE2MCwiYXpwIjoiRDJxMUpXRjdmeXV0dm01TXVFNkVZUjZtYkhuUHk1alEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZWRpdDphY3RvciIsImVkaXQ6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.qeiba00JU-Dix8qvmdrNWJBrCfJbvLsAoSPbNgRUMyEAx-g1xz1T-MQ9E5kCjuaurGLReq1LVvB6oJhiRkTjzDSSOE4hegtXVUCeujZKeoMCUaJ2g7X2_RzA24qc0CH1V9wvsdj3iNcThIQufch4fC6XNuk-K-hYNP_Nz2majc_UxCtbB5isL9yDoN-73kB5naMa2x4Wregub0E_9LNkhpVUkG2svrKpUNLEBNVuKbvj3DxEs21vuZSp0MjHPmO2q4YYzvLPIO_00Ab-vFa4gqdCgsLdbA8syfX4Z1RMhhJWjzZ7pvYGGqsXQs4i_-JmALHdtq2bTsoBAONOFX3m3g"
        self.castingDirectorToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EZEROVGsxTUVZeVJEUTVORVV4T1RKRFJFUTVOak00UXpneU1qa3pOakV6UkRWRFJrUkJRdyJ9.eyJpc3MiOiJodHRwczovL2Rldi0tcnB6eHY0ci5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTAxNDcyMzM5MDExMDAzOTkyMjAiLCJhdWQiOlsiaHR0cDovL2xvY2FsaG9zdDo4MDgwLyIsImh0dHBzOi8vZGV2LS1ycHp4djRyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODI0Njg2MDcsImV4cCI6MTU4MjU1NTAwNiwiYXpwIjoiRDJxMUpXRjdmeXV0dm01TXVFNkVZUjZtYkhuUHk1alEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwiZWRpdDphY3RvciIsImVkaXQ6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.w48MVtDNaMdJcJ5-pjReuiw8UWDf9GsKoZyXj6MSCQDEf_yt0L1fFgZDdcBwSO1N34g5JA0NY_IP4yku5kdeciAiH-rTGskW1IZajosA9-FhmNadsyiWAOwxbxAACcfSScX3gaxvzvbIxdgInxc9vxo3jVofRg8qU8LzcQTscgiBGKGkS_v_J6heZMOMsBgVGPgO6ZNfR_6dyD7YvIMaCj-VA9wKVMz2oWgTcW3MeUTcT87u3YkDKbSmO6VihmCOE14VqDsn5bATBgW7kbxyNhGHgJGA3s2ddhQlnYLd-6m7uUNKUFzAT4b4lYA_pSJZBN4Nlao7snPZfuDhGdQyHw"
        self.castingAssistantToken = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EZEROVGsxTUVZeVJEUTVORVV4T1RKRFJFUTVOak00UXpneU1qa3pOakV6UkRWRFJrUkJRdyJ9.eyJpc3MiOiJodHRwczovL2Rldi0tcnB6eHY0ci5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQzMzA2MjM2Njg4ODM5NzcxMDIiLCJhdWQiOlsiaHR0cDovL2xvY2FsaG9zdDo4MDgwLyIsImh0dHBzOi8vZGV2LS1ycHp4djRyLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODI0NzA1MzEsImV4cCI6MTU4MjU1NjkzMCwiYXpwIjoiRDJxMUpXRjdmeXV0dm01TXVFNkVZUjZtYkhuUHk1alEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.URziHNlMps3jkMIXcTR98tjsQZqs3LTK6Uvk6R-jrFOxiAubHqt0wLw9a5u_C5BC_AZIkqo0C4QyOFRj2TI-pbAgOtgq0Jhtay0bRXlTlPZTrv125wto9PWiNACGvENSNPd0n47Cgy2DNxRV8Eg3CytM9TH2pnDRWCJFFjhJaBl67KCOHBbmaluYE-RK6b6RcHfHhaBZ9kGAtIH4BRS6V5QyMxGpy06EUSUA7gIvVpzn3PvpRo_i32a4eKESRPSiF_SX2iFMyotnMDbCU2rGzXZgKD_kwIlUAkS3_gYUcKI4a2Vk9ea_VHUoCBC909xfkxTdUiO4bvXG9hgzaP703w"
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
