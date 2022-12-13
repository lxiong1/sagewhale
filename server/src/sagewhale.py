import os
from time import sleep
from flask import Flask
from dotenv import load_dotenv
from models.subscriber_info_models import db
from apis.subscriber_info_api import api

load_dotenv()

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_PORT}/{POSTGRES_DB}"

db.init_app(app)
api.init_app(app)

with app.app_context():
    for _ in range(30):
        try:
            db.create_all()
        except:
            sleep(1)

if __name__ == "__main__":
    app.run()
