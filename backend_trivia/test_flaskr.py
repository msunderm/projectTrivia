import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}/{}".format('student:student@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            "question" : "Dit this work?",
            "answer":"yes",
            "difficulty":1,
            "category":1
            }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    """1/ For paginated questions"""

    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_get_paginated_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])

    
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get("/question?page=980", json={"id": 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    """2/ To delete a question""" 
    def test_delete_question(self):
        res = self.client().delete("/questions/20")
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 19)
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])
        self.assertEqual(question, None)

    def test_422_if_question_does_not_exist(self):
        res = self.client().delete("/questions/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable") 

    """3/ Create a new question""" 
    def test_create_new_question(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)
    
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])

    def test_405_if_question_creation_not_allowed(self):
        res = self.client().post("/questions/45", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")


    """4/ Question search""" 
    def test_get_question_search_with_results(self):
        res = self.client().post("/questions", json={"searchTerm": "Title"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_get_question_search_without_results(self):
        res = self.client().post("/questions", json={"searchTerm": 'Maxine'})
        data = json.loads(res.data)

        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_questions"], 0)

    def test_get_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['current_category'], 'Science')
        self.assertEqual(data['success'], True)

    def test_get_404_questions_by_category(self):
        res = self.client().get('/categories/10000/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)    


    """5/ Play the quiz"""    
    def test_play_quiz(self):
        quiz_round = {'previous_questions': [], 'quiz_category': {'type': 'Art' ,'id': 2}}
        res = self.client().post('/play', json=quiz_round)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_quiz(self):
        res = self.client().post('/play', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')    



        




   
    



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()