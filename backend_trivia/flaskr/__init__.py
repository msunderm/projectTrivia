import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

db = SQLAlchemy()

def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={'/': {'origins': '*'}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,PATCH,DELETE,OPTIONS"
        )
        response.headers.add("Acces-Control-Allow-Origins", "*")
        return response

    @app.route("/")
    def hello():
        return "hello"
    """
    @TODO: Set up CORS. Allow '*' for origins.
    Delete the sample route after completing the TODOs
    """
    """
    @TODO:Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route("/categories", methods=['GET'])
    def all_categories():
        categories = Category.query.order_by(Category.type).all()
        all_categories = {}

        for category in categories:
            all_categories[category.id] = category.type

        if len(all_categories) == 0:
            abort(404)
        return jsonify({
            "success": True,
            "categories": all_categories,
        })
    """
    @TODO: Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    """

    @app.route("/questions", methods=['GET'])
    def retrieve_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

        categories = Category.query.order_by(Category.id).all()
        all_categories = {}

        if len(current_questions) == 0:
            abort(404)

        for category in categories:
            all_categories[category.id] = category.type

        return jsonify(
            {
                "success": True,
                "questions": current_questions,
                "total_questions": len(Question.query.all()),
                "categories": all_categories,
                "current_category": category.type,
            }
        )
    """
    http://127.0.0.1:5000/questions?page=2 works, also in postman
    """
    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.
    -X DELETE http://127.0.0.1:5000/page/2 command
    """
    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "deleted": question_id,
                    "questions": current_questions,
                    "total_questions": len(Question.query.all()),
                }
            )

        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.
    """
    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    """
    @app.route("/questions", methods=["POST"])
    def get_questionsForSearch():
        body = request.get_json()
        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_difficulty = body.get("difficulty", None)
        new_category = body.get("category", None)
        searchTerm = body.get("searchTerm", None)

        try:
            if searchTerm:
                selection = Question.query.filter(Question.question.ilike(f"%{searchTerm}%")).all()
                current_questions = paginate_questions(request, selection)

                return jsonify(
                    {
                        "success": True,
                        "questions": current_questions,
                        "total_questions": len(current_questions),
                    }
                )

            else:
                question = Question(question=new_question, answer=new_answer,
                difficulty=new_difficulty, category=new_category)
                question.insert()
                selection = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, selection)

                return jsonify(
                    {
                        "success": True,
                        "created": question.id,
                        "question_created": question.question,
                        "questions": current_questions,
                        "total_questions": len(Question.query.all()),
                    }
                )

        except:
            abort(422)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.
    """
    @app.route("/categories/<int:category_id>/questions", methods=["GET"])
    def get_questions(category_id):
        category = Category.query.filter_by(id=category_id).one_or_none()

        if category is None:
            abort(404)

        try:
            selection = Question.query.filter_by(category=category.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(Question.query.all()),
                'current_category': category.type,
            })

        except:
            abort(422)
    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    """
    @app.route('/play', methods=['POST'])
    def quiz_game():
        try:
            body = request.get_json()
            previous_questions = body.get('previous_questions', None)
            category = body.get('quiz_category', None)
            category_id = category['id']
            next_question = None

            if category_id != 0:
                questions = Question.query.filter_by(category=category_id).filter(Question.id.notin_((previous_questions))).all()
            else:
                questions = Question.query.filter(Question.id.notin_((previous_questions))).all()

            if len(questions) > 0:
                next_question = random.choice(questions).format()

            return jsonify({
                "question": next_question,
                "success": True,
            })

        except:
            abort(422)
    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False, "error": 404, "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False, "error": 422, "message": "unprocessable"
            }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False, "error": 400, "message": "bad request"
            }), 400

    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
            "success": False, "error": 405, "message": "method not allowed"
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False, "error": 500, "message": "internal server error"
            }), 500

    return app
