from dotenv import load_dotenv
import os
load_dotenv()
DB_NAME = os.environ.get("trivia")
DB_USER=os.environ.get("student")
DB_PASSWORD = os.environ.get("student")