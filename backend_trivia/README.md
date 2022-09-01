# Project - Trivia API
## Setting up the Backend
### Install dependencies
1. Python 3.7 - Follow instructions to install the latest version of python for your platform in the python docs

2. Virtual Environment - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the python docs

3. PIP Dependencies - Once your virtual environment is setup and running, install the required dependencies by navigating to the /backend directory and running:
```
pip install -r requirements.txt
```
### Key Pip Dependencies
Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in app.pyand can reference models.py.

Flask-CORS is the extension we'll use to handle cross-origin requests from our frontend server.

###  Set up the Database
With Postgres running, create a trivia database:

``` 
createdb trivia
``` 
Populate the database using the trivia.psql file provided. From the backend folder in terminal run:

```
psql trivia < trivia.psql
```

### Run the Server
From within the ./src directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
export FLASK_APP = flaskr
export FLASK_ENV = development
flask run
```

## Introduction 
Backend - Trivia API is made for a trivia. The application must be able to display questions but also delete or add new questions. Questions should be searchable by category or based on a text string. Finally, there is a quiz game that can be played.

## Getting started
- Base URL: this backend app is hosted at the default, http://127.0.0.1:5000/, which is sat as a proxy in the frontend configuration. 
- Authentication: this application does not require any authentication 


## Error handling
Errors are returned as JSON objects in the following format: 
```
{
  "success": False,
  "error": 400,
  "message": "bad request"
}
```

The API will return the folowing error types when the request fails: 
- 400: bad request
- 404: resource not found
- 405: method not allowed
- 422: unprocessable
- 500: internal server error

## Resource Endpoint Library 
### GET /categories
- General
  - Request arguments: None
  - Returns: A list of categories where the questions are being organized by with corresponding ID
- Sample: curl http://127.0.0.1:5000/categories
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true
}
```

### GET /questions
- General
  - Request arguments: None
  - Returns the categories with ID.
  - Returns a list of questions, included id, answer, category and difficulty. The current category is displayed. 
  - Result are paginated in groups of 10. Inlcude a request argument to choose page number, starting from 1. 
- Sample: curl http://127.0.0.1:5000/questions

```
 {
  {
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": "History",
    "questions": [
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        }
    ],
    "success": true,
    "total_questions": 23
}

```

### GET /categories/{category_id}/questions
- General: The goal is to retrieve questions based on category. 
- Request arguments: category_id:int
- curl http://127.0.0.1:5000/categories/4/questions
```
{
    "current_category": "Science",
    "questions": [
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": "yes",
            "category": 1,
            "difficulty": 1,
            "id": 24,
            "question": "yes"
        },
        {
            "answer": "yes",
            "category": 1,
            "difficulty": 1,
            "id": 25,
            "question": "Did this postman test work?"
        },
        {
            "answer": "yes",
            "category": 1,
            "difficulty": 1,
            "id": 26,
            "question": "Did this postman test work?"
        },
        {
            "answer": "try again",
            "category": 1,
            "difficulty": 1,
            "id": 28,
            "question": "new question"
        },
        {
            "answer": "try again",
            "category": 1,
            "difficulty": 1,
            "id": 30,
            "question": "new question"
        },
        {
            "answer": "yes!",
            "category": 1,
            "difficulty": 1,
            "id": 32,
            "question": "Test on frontend"
        }
    ],
    "success": true,
    "total_questions": 28
}

```

### DELETE /questions/{question_id}
- General
  - Request arguments: question_id: int
  - Deletes a question with a given ID if it exists. Returns the ID of the deleted question, the success vaue, total questions after deletion, and the other questions based on current page number. 
  - curl -X DELETE http://127.0.0.1:5000/questions/12
```
{
    "deleted": 12,
    "questions": [
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        }
    ],
    "success": true,
    "total_questions": 27
}
```
### POST /questions
- General
  - - Request arguments: {question: string, answer: string, difficulty: int, category: int}
  - Creates a new question using the submitted question, answer, rating and category. Returns the id of the created question, success value, total questions and the list of questions based on the current page number 
  - curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content-Type:application/json" -d '{"question":"Did this work as a test?", "answer":"yes it did", "difficulty":1,"category":2}'
```
{
    "created": 37,
    "question_created": "Did this work as a test?",
    "questions": [
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        }
    ],
    "success": true,
    "total_questions": 28
}

```

### POST /questions
- General
  - Request arguments: {question: string, answer: string, difficulty: int, category: int, searchTerm:string}
  - Searches for a new question using the submitted string. Returns the id of the searched question, success value, total questions and the list of questions based on the current page number
  - curl curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content-Type:application/json" -d '{"question":"Did this work as a test?", "answer":"yes it did", "difficulty":1,"category":2, "searchTerm":"title"}'
```
{
    "questions": [
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
    ],
    "success": true,
    "total_questions": 1
}
```

### POST /play
- Endpoint to play the trivia game. 
- Request arguments: {previous_questions: array, category: {id:int}}
```
{
  "question": {
    "answer": "The Liver", 
    "category": 1, 
    "difficulty": 4, 
    "id": 20, 
    "question": "What is the heaviest organ in the human body?"
  }, 
  "success": true
}
```

## Deployment N/A
## Authors
Maxine Sundermann

## Acknowledgements
Thank you udacity for the course, as well as Stack Overflow for providing commando's when I was stuck. 

